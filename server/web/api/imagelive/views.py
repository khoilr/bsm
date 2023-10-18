
from fastapi import APIRouter, WebSocket
import time
import threading
import cv2
import base64
import os

from dotenv import load_dotenv
load_dotenv()
class VideoCamera(object):
   def __init__(self, URL):
       self.video = cv2.VideoCapture(URL)
       (self.grabbed , self.frame) = self.video.read()
       self.stop_thread = False
       self.thread = threading.Thread(target=self.update , args=())
       self.thread.start()


   def __del__(self):
       self.stop_thread = True
       self.video.release()
       cv2.destroyAllWindows()

   def get_frame(self):
       image = self.frame
       _ , jpeg = cv2.imencode(' .jpg' , image)
       return jpeg.tobytes()

   def update(self):
       while not self.stop_thread:
            time.sleep(0.05)
            (self.grabbed , self.frame) = self.video.read()

URL = os.getenv("RTSP_URL")

camera = VideoCamera(URL=URL)
router = APIRouter()
@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    global camera
    await websocket.accept()
    while True:
        try:
            frame = camera.get_frame()
            base64_string= base64.b64encode(frame).decode('utf-8')
            await websocket.send_bytes(base64_string)
        except:
            pass

