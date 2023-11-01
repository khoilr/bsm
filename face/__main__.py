import cv2
import pandas as pd
from dotenv import load_dotenv
from loguru import logger

from face.blob import upload_blob
from face.face_handler import *
from face.face_processors.face_detection import detect_faces
from face.face_processors.face_identification import get_face_id
from face.image_processors import draw_info
import redis
from redis_connection import redis_pool

load_dotenv()

# Constants
LOG_FILE = "face/camera.log"
FACES_CSV_FILE = "face/faces.csv"
URL = "rtsp://0.tcp.ap.ngrok.io:10708/user:1cinnovation;pwd:1cinnovation123"
MAX_CAP_OPEN_FAILURES = 10
MAX_READ_FRAME_FAILURES = 10
FRAME_FREQUENCY = 5

df_faces: pd.DataFrame = (
    pd.read_csv(FACES_CSV_FILE)
    if os.path.exists(FACES_CSV_FILE)
    else pd.DataFrame(columns=["timestamp", "face", "facial_area", "confidence", "face_id", "path"])
)

redis_connection = redis.Redis(connection_pool=redis_pool)

# Configure logger
logger.add(LOG_FILE, rotation="500 MB")


def main_processor(frame):
    faces = detect_faces(frame)

    for face in faces:
        face["face_id"] = get_face_id(face, df_faces)
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

        # redis append to stream 'frames'
        redis_connection.xadd("frames", {"url": f"http://localhost:30003/blob/{blob['stored_name']}"})

        logger.info(f"Face detected {face['face_id']}.")

        cv2.imshow("frame", image)


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
