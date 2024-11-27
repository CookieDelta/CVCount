import numpy as np
from ultralytics import YOLO
from sort import Sort
import cv2


class DetectionModel:
    def __init__(self, model_path):
        self.model = YOLO(model_path)
        self.model.to("cuda")
        self.tracker = Sort(max_age=5, min_hits=1, iou_threshold=0.3)

    def detect_objects(self, frame):
        detections = np.empty((0, 5))
        results = self.model(frame, stream=True)
        for result in results:
            for box in result.boxes:
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                conf = float(box.conf[0])
                cls = int(box.cls[0])
                if conf > 0.45:  
                    detections = np.vstack((detections, [x1, y1, x2, y2, conf]))
        return detections

    def track_objects(self, detections, frame):
        tracked_objects = self.tracker.update(detections)
        results = []
        for obj in tracked_objects:
            x1, y1, x2, y2, obj_id = map(int, obj)
            cx, cy = (x1 + x2) // 2, (y1 + y2) // 2
            cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 255), 2)
            cv2.circle(frame, (cx, cy), 5, (255, 0, 255), cv2.FILLED)
            results.append((x1, y1, x2, y2, obj_id, cx, cy))
        return results
