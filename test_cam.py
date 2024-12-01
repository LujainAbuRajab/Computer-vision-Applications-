import cv2
video = cv2.VideoCapture(0)
if not video.isOpened():
    print("Error: Cannot access the camera")
else:
    print("Camera is accessible!")
video.release()
