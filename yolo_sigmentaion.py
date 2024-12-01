from ultralytics import YOLO

# Load YOLOv8 segmentation model
model = YOLO('yolov8n-seg.pt')

# Run predictions on webcam (or replace '0' with a video file path)
model.predict(source=0, show=True, conf=0.4, device='cpu')

