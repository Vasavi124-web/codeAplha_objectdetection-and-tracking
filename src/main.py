import cv2
import os

from detector import VehicleDetector
from tracker import VehicleTracker
from utils import draw_tracked_objects

def main():
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    video_path = os.path.join(BASE_DIR, "data", "video01.mp4")

    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("Error: Could not open video.")
        return
    
    detector = VehicleDetector()
    tracker = VehicleTracker()
    cv2.namedWindow("Vehicle Detection and Tracking", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Vehicle Detection and Tracking", 1000, 600)
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        detections = detector.detect(frame)
        tracked_objects = tracker.update(detections)
        frame = draw_tracked_objects(frame, tracked_objects)
       
        cv2.imshow("Vehicle Detection and Tracking", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()


    