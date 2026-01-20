import pyautogui
import cv2  # Correct import (not 'cv')
import numpy as np

resolution = (1920, 1080)
codec = cv2.VideoWriter_fourcc(*"XVID")
filename = "Recording.avi"
fps = 60.0

out = cv2.VideoWriter(filename, codec, fps, resolution)

cv2.namedWindow("Live", cv2.WINDOW_NORMAL)  # Fixed: 'namedWindow' not 'namedWINDOW'
cv2.resizeWindow("Live", 480, 270)

while True:
    img = pyautogui.screenshot()
    # Convert the screenshot to a numpy array
    frame = np.array(img)
    # Convert RGB to BGR (OpenCV uses BGR format)
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)  # Fixed: 'cvtColor' not 'cvColor', and COLOR_RGB2BGR
    out.write(frame)
    cv2.imshow('Live', frame)  # Fixed: 'imshow' not 'inshow'

    if cv2.waitKey(1) == ord('q'):
        break

out.release()
cv2.destroyAllWindows()