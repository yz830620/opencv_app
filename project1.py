## project for using marker to draw a line
## tracking practice

import cv2
frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture(1)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10, 150)

myColors = []

def findColor(img):
    imgHSV = cv.cvtColor(img, cv2.COLOR_BGR2HSV)
    # lower = np.array([h_min, s_mix, v_min])
    # upper = np.array([h_man, s_max, v_max])
    # mask = cv2.inRange(imgHSV, lower, upper)
    # cv.imshow("img", mask)


while True:
    success, img = cap.read()
    cv2.imshow("Result", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


