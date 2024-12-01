# import numpy as np
# import cv2

# #to tell that the video that i wanna process are coming through the labtob camera
# video = cv2.VideoCapture(0)
# #as long as the camera are open-> read from it
# while True:
#     _, frame = video.read()
#     #cose we are doing an edge ditection, is better to conver it to gray
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     # we ganna use "canny" edge ditection 
#     edges = cv2.Canny(gray,100,200)

#     #to marge the frame(in 3d) and the edges(in 2d) we conver the edges to RGB to make it channels
#     edges_3d = cv2.cvtColor(edges, cv2.COLOR_GRAY2RGB)
#     combined = np.hstack((frame,edges_3d))
#     cv2.imshow('video, edges', combined)

#     #to make it stop at some point
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

#     video.release()
#     cv2.destroyAllWindows()


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
