from deepface import DeepFace
from datetime import datetime


def detect_faces(frame) -> list[dict]:
    """
    Return: [{
        face: list,
        facial_area: dict,
        confidence: float,
        timestamp: int
    } ]
    """
    # Extract faces from frame
    face_objs = DeepFace.extract_faces(
        frame,
        detector_backend="opencv",
        enforce_detection=False,
        align=True,
    )

    return [{**face, "timestamp": int(datetime.now().timestamp())} for face in face_objs if face["confidence"] > 0]
