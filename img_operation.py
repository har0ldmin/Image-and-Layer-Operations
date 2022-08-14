from cv2 import COLOR_BGR2RGB
import numpy as np
import cv2


# import img
original_img = cv2.imread('screenshot.png')

copied_img = original_img.copy()    # deep copy : original_img  won't be affected even copied_img is modified


cv2.circle(copied_img, (425, 644), 125, (0,0,0), -1, cv2.LINE_AA)   # -1 : fill in color
                                                                    # (0,0,0) : black
                                                                    # cv2.LINE_AA : gives anti-aliased line which looks great for curves
                                                                    # 125 : size of the circle
                                                                    # (425, 655) : co-ordinates


# resize copied_img
resized_img = copied_img[330:950, 0:770]

# if resized_img is in BGR order, the function will rearrange the pixels into RGB order
resized_img = cv2.cvtColor(resized_img, cv2.COLOR_BGR2RGB)

# RGB -> Grey colored
grey_img = cv2.cvtColor(resized_img, cv2.COLOR_RGB2GRAY)

# save file
cv2.imwrite('new_img.png', grey_img)
