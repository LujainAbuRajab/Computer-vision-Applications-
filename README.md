# :pushpin: Computer Vision Applications: Edge Detection, Object Detection and Segmentation 

This repository contains three separate Python projects that demonstrate various object detection techniques using Canny Edge Detection and YOLO models for object detection and segmentation.

---

## **Project Structure**
```plaintext
.
├── canny_object_detection.py    # Canny Edge Detection Application
├── yolo_object_detection.py     # YOLO Object Detection Application
├── yolo_object_segmentation.py  # YOLO Object Segmentation Application
└── README.md                    # Project Documentation

```
---

## **Prerequisites**
Before running any of the projects, ensure you have the following installed and configured in your environment:

### 1. Anaconda Environment Setup
Create and activate an Anaconda environment:

```bash

conda create -n object_detection_env python=3.9 -y
conda activate object_detection_env

```

### 2. Required Libraries
Install the necessary libraries in the environment:

```bash

pip install numpy opencv-python-headless ultralytics torch torchvision torchaudio
```

- `numpy`: For numerical computations.
* `opencv-python-headless`: For image and video processing.
+ `ultralytics`: For YOLO models.
- `torch`, `torchvision`, `torchaudio`: Required for YOLO's PyTorch-based implementation.

---
## 1.  Canny Edge Detection Application
This application uses OpenCV's Canny edge detection to highlight edges in video frames captured from the webcam.

### File: `canny_object_detection.py`

### Usage:

1. Run the script:
```bash
  python canny_object_detection.py
```

2. Press q to quit the application.

## Features:
- Grayscale conversion of video frames.
* Canny edge detection with adjustable thresholds.
+ Real-time display of the original and edge-detected frames side by side.

---

## 2.  YOLO Object Detection
This application uses the YOLOv8 object detection model to identify objects in real time from the webcam.

### File: `yolo_object_detection.py`

### Usage:

1. Run the script:
```bash
  python yolo_object_detection.py
```

2. Press q to quit the application.

---
## 3. YOLO Object Segmentation
This application uses the YOLOv8 segmentation model to detect and segment objects in real-time from the webcam.

### File: `yolo_object_segmentation.py`

### Usage:

1. Run the script:
```bash
  python yolo_object_segmentation.py

```

2. Press q to quit the application.

---
## Reference
- [OpenCV Documentation](https://github.com/opencv/opencv)
* [YOLOv8 Documentation](https://github.com/ultralytics/ultralytics/blob/main/docs/en/models/yolov8.md)

---
### Let me know if you need help with any specific part of this! 😊  

