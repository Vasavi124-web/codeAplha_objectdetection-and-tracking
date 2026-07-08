import cv2

def draw_tracked_objects(frame, tracked_objects):

    for obj in tracked_objects:
        x1, y1, x2, y2, class_name, track_id = obj
        label = f"{class_name} | ID: {track_id}"

        cv2.rectangle(
            frame,
            (x1,y1),
            (x2,y2),
            (0, 255, 0),
            2
        )

        (text_width, text_height), _ = cv2.getTextSize(
            label,
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            2
        )

        cv2.rectangle(
            frame,
            (x1, y1 - text_height - 10),
            (x1 + text_width, y1),
            (0, 255, 0),
            -1
        )

        cv2.putText(
            frame,
            label,
            (x1, y1-5),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (0, 0, 0),
            2
        )
    
    return frame