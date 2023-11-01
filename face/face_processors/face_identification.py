import os

import numpy as np
import pandas as pd
from deepface import DeepFace
from skimage import io

FACES_CSV_FILE = "face/faces.csv"
PERSONS_CSV_FILE = "face/persons.csv"
FRAME_DIR = "face/images"
FACE_THRESHOLD = 5

# Init DataFrame
df_persons: pd.DataFrame = (
    pd.read_csv(PERSONS_CSV_FILE) if os.path.exists(PERSONS_CSV_FILE) else pd.DataFrame(columns=["face_id", "Name"])
)


def identify_face(frame_1, frame_2) -> bool:
    result = DeepFace.verify(
        frame_1,
        frame_2,
        detector_backend="opencv",
        enforce_detection=False,
    )
    return result["verified"]


def get_face_id(face: dict, df_faces: pd.DataFrame) -> int:
    frame = face["face"]

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
        else:
            threshold = FACE_THRESHOLD

        # count_true is the number of paths that are verified as the same person;
        count_true = 0
        count_false = 0

        # Iterate through paths
        for path in paths:
            if identify_face(
                frame,
                io.imread(f"http://localhost:30003/blob/{path}"),
            ):
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
    return save_new_person(new_id, f"Person {new_id}")["face_id"]


def save_new_person(person_id, person_name):
    new_row = {"face_id": person_id, "name": person_name}
    df_persons.loc[len(df_persons)] = new_row
    df_persons.to_csv(PERSONS_CSV_FILE, index=False)
    return new_row
