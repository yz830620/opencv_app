## project for using marker to draw a line
## tracking practice

import cv2
import numpy as np

frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10, 150)

myColors_dict = {
    "yellow": [21, 80, 0, 40, 225, 225],
    "blue": [94, 135 , 36, 117, 225, 171],
    "green": [36, 69, 76, 69, 224, 183],
    "purple": [118, 99, 89, 138, 166, 225],
    }

def findColor(img, myColors_dict):
    for color in myColors_dict.keys():
        imgHsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        lower = np.array(myColors_dict[color][0:3])
        upper = np.array(myColors_dict[color][3:6])
        mask = cv2.inRange(imgHsv, lower, upper)
        cv2.imshow(color, mask)

# 期待功能:
# 按一個按鈕切換顏色，標記四個顏色的按鈕
while True:
    success, img = cap.read()
    findColor(img, myColors_dict)
    cv2.imshow("Result", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


