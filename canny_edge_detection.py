import numpy as np
import cv2

# Capture video from the laptop camera
video = cv2.VideoCapture(0)

# Check if the camera opened successfully
if not video.isOpened():
    print("Error: Could not open the video stream or file")
    exit()

# Read and process frames as long as the camera is open
while True:
    ret, frame = video.read()
    if not ret:
        print("Error: Failed to capture frame")
        break

    # Convert to grayscale for edge detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Perform Canny edge detection
    edges = cv2.Canny(gray, 100, 200)

    # Convert edges to RGB to merge with the original frame
    edges_3d = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
    combined = np.hstack((frame, edges_3d))

    # Display the video with edges
    cv2.imshow('Video and Edges', combined)

    # Press 'q' to exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources and close windows
video.release()
cv2.destroyAllWindows()
