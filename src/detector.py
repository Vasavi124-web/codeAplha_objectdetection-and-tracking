from ultralytics import YOLO

class VehicleDetector:
    def __init__(self, model_path: str = "../models/yolov8n.pt", conf_threshold: float = 0.45):
        self.model = YOLO(model_path)
        self.conf_threshold = conf_threshold

        self.vehicle_class_ids = {2, 3, 5, 7}


    def detect(self, frame):
        results=self.model(frame)[0]
        detections=[]
        boxes=results.boxes

        if boxes is None:
            return detections

        for box in boxes:
            conf = float(box.conf[0])

            if conf<self.conf_threshold:
                continue

            cls_id = int(box.cls[0])
            class_name = self.model.names[cls_id]

            if cls_id not in self.vehicle_class_ids:
                continue

            x1, y1, x2, y2, = map(int, box.xyxy[0])

            detections.append([x1, y1, x2, y2, conf, class_name])

        return detections
    