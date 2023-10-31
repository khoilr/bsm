import os
import uuid
from datetime import datetime
from typing import Union
import redis
import cv2
import numpy as np
import pandas as pd
import requests
from deepface import DeepFace
from dotenv import load_dotenv
from redis_connection import redis_pool

load_dotenv()

FACES_CSV_FILE = "face/faces.csv"
PERSONS_CSV_FILE = "face/persons.csv"
FRAME_DIR = 'face/images'
FACE_THRESHOLD = 5

BLOB_HOST = os.environ.get("BLOB_HOST", "localhost")
BLOB_PORT = os.environ.get("BLOB_PORT", 30003)

# Init DataFrame
df_faces: pd.DataFrame = (
    pd.read_csv(FACES_CSV_FILE)
    if os.path.exists(FACES_CSV_FILE)
    else pd.DataFrame(columns=["timestamp", "face", "facial_area", "confidence" ,"face_id", "path"])
)
df_persons: pd.DataFrame = (
    pd.read_csv(PERSONS_CSV_FILE) if os.path.exists(PERSONS_CSV_FILE) else pd.DataFrame(columns=["FaceID", "Name"])
)

redis_connection = redis.Redis(connection_pool=redis_pool)

def face_detection(frame) -> list[dict]:
    # Extract faces from frame
    face_objs = DeepFace.extract_faces(
        frame,
        detector_backend="opencv",
        enforce_detection=False,
        align=True,
    )

    return [{**face, "timestamp": int(datetime.now().timestamp())} for face in face_objs if face["confidence"] > 0]

    # Iterate through faces
    for face in face_objs:
        # Skip if confidence is 0 or infinity

        if face["confidence"] <= 0:
            continue

        # Set is_change to True
        is_change = True

        # Save frame to file
        frame_path = save_image(frame=frame)

        # Create row to add to df_faces
        new_face_row = {
            "Datetime": int(datetime.now().timestamp()),
            "FrameFilePath": frame_path,
            "Confidence": face["confidence"],
            "X": (face["facial_area"]["x"]),
            "Y": face["facial_area"]["y"],
            "Width": face["facial_area"]["w"],
            "Height": face["facial_area"]["h"],
        }

        face_id = face_recognition(frame)

        new_face_row["FaceID"] = face_id
        df_faces.loc[len(df_faces)] = new_face_row

    # detected successfully
    if is_change:
        # handleFaceDetected(new_face_row)
        df_faces.to_csv(FACES_CSV_FILE, index=False)


def face_recognition(frame):
    # Extract distinct value of face ID
    distinct_face_id = df_faces["face_id"].dropna().unique()

    # Shuffle distinct face ID
    np.random.shuffle(distinct_face_id)

    # Get max face ID or 0 if there is no face ID
    max_id = max(distinct_face_id) if len(distinct_face_id) > 0 else 0

    # Iterate through distinct face ID
    for face_id in distinct_face_id:
        # Get image paths of this face ID
        paths = df_faces.loc[df_faces["face_id"] == face_id]["path"].values

        # threshold is the minimum of number of paths and FACE_THRESHOLD
        if len(paths) < FACE_THRESHOLD:
            threshold = len(paths)
            threshold_distance = 0.5
        else:
            threshold = FACE_THRESHOLD
            threshold_distance = None

        # count_true is the number of paths that are verified as the same person;
        count_true = 0
        count_false = 0

        # Iterate through paths
        for path in paths:
            # Verify similarity between a pair of images using DeepFace library
            result = DeepFace.verify(
                frame,
                path,
                model_name="ArcFace",
                detector_backend="opencv",
                enforce_detection=False,
            )

            # When threshold distance is not None, then verify by distance. Otherwise, verify by verified
            if threshold_distance is not None:
                # If distance is less than threshold_distance, count_true += 1
                # Else count_false += 1
                if result["distance"] < threshold_distance:
                    count_true += 1
                else:
                    count_false += 1
            else:
                # If verified is True, count_true += 1
                # Else count_false += 1
                if result["verified"]:
                    count_true += 1
                else:
                    count_false += 1

            # If count_true is equal to threshold, return face_id
            # Else if count_false is equal to threshold, break
            if count_true == threshold:
                return face_id
            elif count_false == threshold:
                break

    new_id = max_id + 1
    new_row = {"FaceID": new_id, "Name": new_id}
    df_persons.loc[len(df_persons)] = new_row
    df_persons.to_csv(PERSONS_CSV_FILE, index=False)

    return new_id


def draw_info(frame, face, face_id):
    x = face['facial_area']['x']
    y = face['facial_area']['y']
    w = face['facial_area']['w']
    h = face['facial_area']['h']
    
    extedned_bbox=  calculate_extended_bbox(x, y, w, h, frame.shape, extend_by=20)
    
    # draw rectangle wrap face
    rectangle = cv2.rectangle(
        frame,
        (extedned_bbox[0], extedned_bbox[1]),
        (extedned_bbox[0] + extedned_bbox[2], extedned_bbox[1] + extedned_bbox[3]),
        (0, 255, 0),
        2,
    )
    
    # write name on the rectangle
    cv2.putText(
        rectangle,
        f"FaceID: {face_id}",
        (extedned_bbox[0] - 10, extedned_bbox[1] - 10),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.5,
        (0, 255, 0),
        2,
    )

    return rectangle
    
    

# Save an image to a specified directory
def save_image(frame, save_dir: str = ".", name: str = None) -> Union[str, None]:
    if name is None:
        _uuid = uuid.uuid4()
        uuid_str = str(_uuid)
        image_path = f"{save_dir}/{uuid_str}.jpg"
    else:
        image_path = f"{save_dir}/{name}.jpg"

    try:
        cv2.imwrite(image_path, frame)

        with open(image_path, "rb") as f:
            url = f"http://{BLOB_HOST}:{BLOB_PORT}/upload"
            method = "POST"
            files = {"file": f}
            response = requests.request(
                method,
                url,
                files=files,
                timeout=60,
            )
            
            stored_name = response.json().get("stored_name")
            
            # store to redis stream
            redis_connection.xadd("frame", {"frame": stored_name})

            return image_path
        
    except Exception as e:
        return None


def main_processor(frame):
    faces = face_detection(frame)

    for face in faces:
        face_id = face_recognition(frame)
        new_frame = draw_info(frame, face)
        save_image(new_frame, save_dir=FRAME_DIR, name=face_id)
        
        df_faces.loc[len(df_faces)] = {**face, "face_id": face_id}

    df_faces.to_csv(FACES_CSV_FILE, index=False)
