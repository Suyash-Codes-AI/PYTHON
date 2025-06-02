import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
# This code demonstrates how to convert an image from BGR to various color spaces using OpenCV.

# Make sure to have OpenCV installed in your Python environment.
# You can install it using pip if you haven't done so:
# pip install opencv-python
# Import necessary libraries
# OpenCV is used for image processing
# NumPy is used for numerical operations
# Matplotlib is used for displaying images
# Read an image in BGR format




# Load an image in BGR format
img = cv.imread('PHOTOS/cat.jpg')
cv.imshow('cat',img)


#BGR to Grayscale

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

#BGR to HSV(Hue, Saturation, Value)

hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow('HSV',hsv)

#BGR to LAB(CIE L*a*b*) (CIE stands for Commission Internationale de l'Éclairage)

Lab = cv.cvtColor(img,cv.COLOR_BGR2Lab)
cv.imshow('LAB',Lab)

#BGR to RGB 

rgb = cv.cvtColor(img,cv.COLOR_BGR2RGB)
cv.imshow('RGB',rgb)


plt.imshow(img)
plt.show()


cv.waitKey(0) 
 # Wait for a key press to close the window

#We cannot convert GRAY to HSV, LAB, or RGB directly.
# We need to convert it back to BGR first.
#BGR to GRAY to BGR


#HSV TO BGR 					      	 	 	 	 	

hsv_bgr = cv.cvtColor(hsv,cv.COLOR_HSV2BGR)
cv.imshow('HSV to BGR', hsv_bgr)    
