import cv2 as cv
import numpy as np
#events = [print(i) for i in dir(cv2) if 'EVENT' in i]

drawing = False
mode = True
ix, iy = -1, -1
guide_line = []

def draw_circle(event, x, y, flags, param):
    global ix,iy, drawing, mode, guide_line, ori_img
    if event==cv.EVENT_LBUTTONDOWN:
        ori_img = img.copy()
        drawing = True
        ix, iy = x, y
    elif event==cv.EVENT_MOUSEMOVE and flags==cv.EVENT_FLAG_LBUTTON:
        if drawing == True:
            cv.circle(img,(x, y), 1, (0,0,255), -1)
            guide_line.append((x, y))
    elif event==cv.EVENT_LBUTTONUP:
        drawing == False
        if mode == True:
            # min_y, max_y, min_x, max_x = get_portion(x, y, ix, iy)
            # img[min_y:max_y, min_x:max_x] = ori_img[min_y:max_y, min_x:max_x]
            img[:,:] = ori_img[:,:]
            cv.rectangle(img,(ix,iy), (x,y), (0,255,0), 3)
            # for x,y in guide_line:
            #     print(x,y)
            #     cv.circle(img,(x, y), 1, (0,0,0), -1)
            
            guide_line = []
        else:
            r = int(np.sqrt((x-ix)**2+(y-iy)**2))
            cv.circle(img, (x,y), 3, (0,0,255), -1)

def get_portion(x1, y1, x2, y2):
    min_x = min(x1, x2)
    max_x = max(x1, x2)
    min_y = min(y1, y2)
    max_y = max(y1, y2)
    return min_y, max_y, min_x, max_x

img = np.zeros((512, 512, 3), np.uint8)
cv.namedWindow('image')
cv.setMouseCallback('image', draw_circle)
#ori_img = np.zeros((512, 512, 3), np.uint8)+255


while(1):
    cv.imshow('image', img)
    k = cv.waitKey(1)&0xFF
    if k == ord('m'):
        mode = not mode
    
    elif k == 27:
        break

cv.destroyAllWindows()