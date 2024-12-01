from ultralytics import YOLO

# Load YOLOv8 object detection model
model = YOLO('yolov8n.pt')

# Run predictions on webcam 
model.predict(source=0, show=True, conf=0.4, device='cpu')

