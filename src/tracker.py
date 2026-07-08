import numpy as np
from sort import Sort

class VehicleTracker:
    def __init__(self):
        self.tracker = Sort()
    
    def update(self, detections):
        if len(detections) == 0:
            return []
        
        dets = []
        class_map = {}

        for i, det in enumerate(detections):
            x1, y1, x2, y2, conf, class_name = det
            dets.append([x1, y1, x2, y2, conf])
            class_map[i] = class_name

        dets = np.array(dets)

        tracks = self.tracker.update(dets)
        tracked_objects = []

        for track in tracks:
            x1, y1, x2, y2, track_id = track
            track_id = int(track_id)

            best_class = "vehicle"

            for i, det in enumerate(detections):
                dx1, dy1, dx2, dy2, conf, class_name = det
                if abs(dx1-x1) < 50 and abs(dy1-y1) < 50:
                    best_class = class_name
                    break
            
            tracked_objects.append([
                int(x1), int(y1), int(x2), int(y2),
                best_class,
                track_id
            ])

        return tracked_objects