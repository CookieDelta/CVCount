class Config:
    DEFAULT_WIDTH = 1920
    DEFAULT_HEIGHT = 1080
    USE_RTSP = False  # True -> RTSP else Webcam (0 for default webcam)
    RTSP_URL = "rtsp://camera_ip:554/stream"  # Port can change (554, 81, 34567), path to stream (/stream)
    YOLO_MODEL_PATH = "yolov8n.pt"
    OUTPUT_VIDEO_PATH = "output/output_video.mp4"
    MASK_PATH = "mask.png"
    DATABASE_CONFIG = {}
    COUNTING_LINE = {
        "x_min": 1000, "x_max": 1172,
        "y_min": 550, "y_max": 623
    }
