from deepface import DeepFace

def identify_face(frame_1, frame_2) ->bool: 
    result = DeepFace.verify(
        frame_1, frame_2, 
        model_name="ArcFace",
                detector_backend="opencv",
                enforce_detection=False,
            )
    return result["verified"]
