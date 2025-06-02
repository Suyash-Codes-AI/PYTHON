import cv2 as cv
import numpy as np
img = cv.imread('PHOTOS/cat.jpg')

#In OpenCV, contours are curves joining all the continuous points along a boundary which have the same color or intensity. They're very useful in shape analysis, object detection, and recognition.
gray = cv.cvtColor(img,cv.COLOR_BGRGRAY)
cv.imshow('Gray',gray)

canny = cv.Canny(img,125,175)
cv.imshow('Canny',canny)

# Find contours in the image

contours,hierarchies = cv.findContours(canny,cv.RETR_LIST,cv.NORMAL_CLONE_WIDE)

print(f'{len(contours)} contour(s) found!')






cv.waitKey(0)  # Wait for a key press to close the window
