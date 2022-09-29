import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame,(640,480))
    print ("ok")

cap.release()
cv2.destroyAllWindows