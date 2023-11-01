import os

import cv2
from loguru import logger
import os 
from dotenv import load_env
from face.face_handler import *
from face.face_processors.face_detection import detect_faces
from face.face_processors.face_identification import identify_face

load_env()

# Constants
LOG_FILE = "camera.log"
FACES_CSV_FILE = "faces.csv"
PERSONS_CSV_FILE = "persons.csv"
URL = "rtsp://0.tcp.ap.ngrok.io:10708/user:1cinnovation;pwd:1cinnovation123"
MAX_WORKERS = 4
MAX_CAP_OPEN_FAILURES = 10
MAX_READ_FRAME_FAILURES = 10
FRAME_FREQUENCY = 5
FACE_THRESHOLD = 5


# Configure logger
logger.add(LOG_FILE, rotation="500 MB")

def main_processor (frame) : 
     faces = detect_faces(frame)
     
     for face in faces:
         print(face)

# Main function to capture frames, process faces, and save results
def main():
    """Handle errors and restart the camera if necessary."""

    frame_counter = 0
    read_frame_failures_counter = 0
    cap_open_counter = 0

    while cap_open_counter < MAX_CAP_OPEN_FAILURES:
        cap = cv2.VideoCapture(URL)

        if not cap.isOpened():
            logger.error("Failed to connect to the camera.")
            cap_open_counter += 1
            continue

        logger.info("Connected to the camera.")
        cap_open_counter = 0
        read_frame_failures_counter = 0

        while read_frame_failures_counter < MAX_READ_FRAME_FAILURES:
            ret, frame = cap.read()

            if not ret:
                logger.error("Failed to capture frame.")
                read_frame_failures_counter += 1
                continue
            else:
                read_frame_failures_counter = 0

            frame_counter += 1

            if frame_counter % FRAME_FREQUENCY == 0:
                main_processor(frame)

            if cv2.waitKey(1) == ord("q"):
                break

        logger.error(f"Read frame failures reached {MAX_READ_FRAME_FAILURES}. Restarting the camera...")

    logger.error(f"Capture open failures reached {MAX_CAP_OPEN_FAILURES}. Exiting the program...")


if __name__ == "__main__":
    main()
