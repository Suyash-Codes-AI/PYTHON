import cv2 as cv
import numpy as np
img = cv.imread('PHOTOS/cat.jpg')
# Convert the image to grayscale



gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)#

# Apply Gaussian blur to the grayscale image

blur = cv.GaussianBlur(img,(9,9),cv.BORDER_DEFAULT)

canny = cv.Canny(img,125,90)

#Dialate the edges detected by Canny
dilated = cv.dilate(canny,(7,9) , iterations = 3)
cv.imshow('dialted',dilated)

#resize the image 
resized = cv.resize(img,(200,1000))
cv.imshow('resized',resized)

#crop the image 
 
cropped = img[50:200,200:787]
cv.imshow('cropped',cropped)


cv.imshow('canny',canny)
cv.imshow('Blur',blur)
cv.waitKey(0)  # Wait for a key press to close the window
