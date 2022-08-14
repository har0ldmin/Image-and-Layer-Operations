import sys
import numpy as np
import cv2


oldx = oldy = -1

def on_mouse(event, x, y, flags, param):
    global oldx, oldy

    if event == cv2.EVENT_LBUTTONDOWN:
        oldx, oldy = x, y
        print('EVENT_LBUTTONDOWN 2: %d, %d' % (x, y))

    elif event == cv2.EVENT_LBUTTONUP:
        print('EVENT_LBUTTONUP 2: %d, %d' % (x, y))

    elif event == cv2.EVENT_MOUSEMOVE:
        if flags & cv2.EVENT_FLAG_LBUTTON:
            cv2.line(img, (oldx, oldy), (x, y), (0, 0, 0), 4, cv2.LINE_AA) 
            cv2.imshow('image', img)
            oldx, oldy = x, y


# set display
img = np.ones((1080, 1080, 3), dtype=np.uint8) * 255

cv2.namedWindow('image')

# third parameter of setMouseCallBack() is a 'callback function';  It is an optional parameter that will be delivered to on_mouse()
cv2.setMouseCallback('image', on_mouse, img)    # we can set 'img' as global in on_mouse(), then we do not have to define the third parameter here

cv2.imshow('image', img)
cv2.waitKey()
cv2.destroyAllWindows()
