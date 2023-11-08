import os

import cv2
import pandas as pd
from dotenv import load_dotenv
from loguru import logger
import requests
from face.blob import upload_blob
from face.face_processors.face_detection import detect_faces
from face.face_processors.face_identification import get_face_info
from face.image_processors import draw_info

load_dotenv()

# Environment variables
server_scheme = os.environ.get("SERVER_SCHEME", "http")
server_url = os.environ.get("SERVER_URL", "localhost")
server_port = os.environ.get("SERVER_PORT", 30000)

# Constants
LOG_FILE = "face/camera.log"
FACES_CSV_FILE = "face/faces.csv"
URL = "rtsp://0.tcp.ap.ngrok.io:10708/user:1cinnovation;pwd:1cinnovation123"
MAX_CAP_OPEN_FAILURES = 10
MAX_READ_FRAME_FAILURES = 10
FRAME_FREQUENCY = 5

# DataFrame faces configuration
df_faces: pd.DataFrame = (
    pd.read_csv(FACES_CSV_FILE)
    if os.path.exists(FACES_CSV_FILE)
    else pd.DataFrame(columns=["timestamp", "face", "facial_area", "confidence", "face_id", "path"])
)

# Configure logger
logger.add(LOG_FILE, rotation="500 MB")


def main_processor(frame):
    faces = detect_faces(frame)

    for face in faces:
        face_info = get_face_info(face, df_faces)
        face["name"] = face_info["name"]
        face["face_id"] = face_info["face_id"]
        image = draw_info(frame, face)
        frame_path = "face/images/frame.jpg"

        # write to blob
        cv2.imwrite(frame_path, image)
        blob = upload_blob(frame_path)
        os.remove(frame_path)

        df_faces.loc[len(df_faces)] = {
            **face,
            "path": blob["stored_name"],
        }
        df_faces.to_csv(FACES_CSV_FILE, index=False)

        # send a post request to server endpoint /api/log
        payload = {"video_url": "", "image_id": blob["stored_name"], "event_id": 4, "face": face["face_id"]}
        method = "post"
        url = f"{server_scheme}://{server_url}:{server_port}/api/log"
        requests.request(method, url, json=payload, timeout=30)

        logger.info(f"Face detected {face['face_id']}.")


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
