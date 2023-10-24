from typing import Awaitable, Callable
import json
from fastapi import FastAPI
from loguru import logger
from server.services.redis.lifetime import init_redis, shutdown_redis
from server.web.api.imagelive.socketmanager import SocketManager
import cv2
import threading
import time
import os
import base64
import socketio
from dotenv import load_dotenv

load_dotenv()


class VideoCamera(object):
    def __init__(self, URL):
        self.video = cv2.VideoCapture(URL)
        (self.grabbed, self.frame) = self.video.read()
        self.stop_thread = False
        self.thread = threading.Thread(target=self.update, args=())
        self.thread.start()

    def __del__(self):
        self.stop_thread = True
        self.video.release()
        cv2.destroyAllWindows()

    def get_frame(self):
        image = self.frame
        _, jpeg = cv2.imencode(' .jpg', image)
        return jpeg.tobytes()

    def update(self):
        while not self.stop_thread:
            time.sleep(0.05)
            (self.grabbed, self.frame) = self.video.read()

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

URL = "rtsp://0.tcp.ap.ngrok.io:10708/user:1cinnovation;pwd:1cinnovation123"
camera = VideoCamera(URL=URL)
def handleConnectedCLient(sio, sid, *args, **kwargs):
    global camera
    try:
        frame = camera.get_frame()
        base64_string = base64.b64encode(frame).decode('utf-8')
        response = {"type": "base64", "data": base64_string}
        return json.dumps(response)
    except:
        camera = VideoCamera(URL=URL)
        return ''

def register_socket_from_app(app: FastAPI):
    """
    Register socket io to app

    Args:
        app (FastAPI): FastAPI app
    """
    sio = socketio.AsyncServer(async_mode="asgi", cors_allowed_origins=[])
    sio_app = socketio.ASGIApp(socketio_server=sio)
    app.mount("/ws", sio_app)
    CONNECTED_SOCKETS = []

    @sio.event
    async def connect(sid, environ, auth):
        print("Client connect with id: " + sid)
        CONNECTED_SOCKETS.append(sid)
        await sio.emit('message', 'connected successfull with id' + sid)
        # await handleConnectedCLient(sio=sio, sid=sid)

    @sio.event
    def disconnect(sid):
        print("disconnect", sid)
        CONNECTED_SOCKETS.remove(sid)

    @sio.on('live_data')
    async def subscribe(sid, data):
        print("Subscribe live data event")
        while True and (sid in CONNECTED_SOCKETS):
            # print('socket ', sid, " send new data")
            data = handleConnectedCLient(sio, sid)
            await sio.send(data=data)
        print('Socket with ID '+sid+" close event")
