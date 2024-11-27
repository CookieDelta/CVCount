# CVCount
SneakPeek to a CV project

# Object Counting with YOLO - Sneak Peek

This repository provides a glimpse into a private project that leverages Computer Vision and YOLO (You Only Look Once) for object detection and tracking. The project demonstrates key components used in processing video feeds, applying masks, and counting objects using advanced detection and tracking techniques.

⚠️ **Note:** Due to the private nature of this project, specific details about the objectives and implementation cannot be disclosed. Below is an overview of the shared scripts and their functionality.

---

## Project Components

### 1. **`config.py`**
This file contains the `Config` class, which defines configuration constants and settings used across the project. It includes parameters for:
- Video settings, including dimensions and source configurations (e.g., RTSP URL or webcam).
- YOLO model path for object detection.
- Output paths for videos and mask files.
- Region of Interest (ROI) coordinates for counting lines.

---

### 2. **`mask.py`**
This script defines the `MaskApplier` class, which handles the selection and application of a region of interest (ROI) mask on video frames. It provides an interactive interface for users to define a polygon mask manually and save it for later use.

**Key Features:**
- Interactive ROI selection with mouse clicks.
- Mask creation and saving functionality.
- Support for video sources from webcams or RTSP streams.

---

### 3. **`detection.py`**
This script defines the `DetectionModel` class, integrating YOLOv8 for object detection and the SORT algorithm for object tracking. It provides tools to detect and track objects in real-time from video feeds.

**Key Features:**
- Object detection using YOLOv8.
- Object tracking using the SORT algorithm.
- Annotation of detections and tracked objects directly on video frames.

---

## Requirements
- Python 3.8+
- OpenCV
- Ultralytics' YOLO
- SORT implementation

---

This repository serves as a starting point to explore the integration of YOLO and object tracking algorithms in real-world applications. As this is a sneak peek, additional scripts and details are not included.
