from typing import Awaitable, Callable
import json
from fastapi import FastAPI
from loguru import logger
from server.services.redis.lifetime import init_redis, shutdown_redis
from server.web.api.imagelive.socketmanager import SocketManager
from database.dao.camera import CameraDAO
import cv2
import threading
import time
import os
import base64
import socketio
from dotenv import load_dotenv
from loguru import logger
import asyncio 
from redis.asyncio import ConnectionPool, Redis
load_dotenv()


class VideoCamera(object):
    def __init__(self, URL):
        self.video = cv2.VideoCapture(URL)
        (self.grabbed, self.frame) = self.video.read()
        self.stop_thread = False
        self.paused = False
        self.lock = threading.Lock()  
        self.thread = threading.Thread(target=self.update, args=())
        self.thread.start()

    def __del__(self):
        self.stop_thread = True
        self.thread.join()  
        self.video.release()
        cv2.destroyAllWindows()

    def get_frame(self):
        with self.lock:
            image = self.frame
            _, jpeg = cv2.imencode('.jpg', image)
            return jpeg.tobytes()

    def update(self):
        while not self.stop_thread:
            with self.lock:
                if self.paused:
                    continue
            time.sleep(0.05)
            (self.grabbed, self.frame) = self.video.read()

    def stop(self):
        with self.lock:
            self.stop_thread = True

    def continue_thread(self):
        with self.lock:
            self.paused = False

    def pause(self):
        with self.lock:
            self.paused = True


def register_startup_event(
    app: FastAPI,
) -> Callable[[], Awaitable[None]]:  # pragma: no cover
    """
    Actions to run on application startup.

    This function uses fastAPI app to store data
    in the state, such as db_engine.

    :param app: the fastAPI application.
    :return: function that actually performs actions.
    """

    @app.on_event("startup")
    async def _startup() -> None:  # noqa: WPS430
        app.middleware_stack = None
        init_redis(app)
        app.middleware_stack = app.build_middleware_stack()
        pass  # noqa: WPS420

    return _startup


def register_shutdown_event(
    app: FastAPI,
) -> Callable[[], Awaitable[None]]:  # pragma: no cover
    """
    Actions to run on application's shutdown.

    :param app: fastAPI application.
    :return: function that actually performs actions.
    """

    @app.on_event("shutdown")
    async def _shutdown() -> None:  # noqa: WPS430
        await shutdown_redis(app)
        pass  # noqa: WPS420

    return _shutdown



def handleConnectedCLient(camera:VideoCamera, *args, **kwargs):
    try:
        frame = camera.get_frame()
        base64_string = base64.b64encode(frame).decode('utf-8')
        response = {"type": "base64", "data": base64_string}
        return json.dumps(response)
    except:
        return ''

def register_socket_from_app(app: FastAPI):
    """
    Register socket io to app.

    Args:
        app (FastAPI): FastAPI app
    """
    sio = socketio.AsyncServer(async_mode="asgi", cors_allowed_origins="*")
    sio_app = socketio.ASGIApp(socketio_server=sio)
    app.mount("/ws", sio_app)
    CONNECTED_SOCKETS = []
    camera_list = {}
    @sio.event
    async def connect(sid, environ, auth):
        print("Client connect with id: " + sid)
        CONNECTED_SOCKETS.append(sid)
        await sio.emit('message', 'connected successfull with id' + sid)

    @sio.event
    def disconnect(sid):
        print("disconnect", sid)
        CONNECTED_SOCKETS.remove(sid)

    @sio.on('live_data')
    async def subscribe(sid, data):
        print("Subscribe live data event")
        if data in camera_list:
            camera_model = await CameraDAO.get(camera_id=int(data))
            camera_list[data] = VideoCamera(camera_model.connect_uri)
        prev_value = None
        redis_pool = app.state.redis_pool
        async with Redis(connection_pool=redis_pool) as redis:
            while sid in CONNECTED_SOCKETS:
                current_value = await redis.get('frames') 
                if prev_value != current_value:
                    data = current_value
                    return sio.send(data=data)
                else:
                    data = handleConnectedCLient(camera_list[data])
                    await sio.send(data=data)
        print('Socket with ID '+sid+" close event")
