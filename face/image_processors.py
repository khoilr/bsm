import cv2


def calculate_extended_bbox(x, y, w, h, frame_shape, extend_by=20) -> tuple:
    extended_x = max(0, x - extend_by)
    extended_y = max(0, y - extend_by)
    extended_w = min(frame_shape[1] - extended_x, w + 2 * extend_by)
    extended_h = min(frame_shape[0] - extended_y, h + 2 * extend_by)

    return extended_x, extended_y, extended_w, extended_h


def draw_info(frame, face):
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