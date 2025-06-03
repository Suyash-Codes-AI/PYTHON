import cv2 as cv
import numpy as np

# Read the image

img = cv.imread('PHOTOS/billu1.jpeg')
cv.imshow('billu1',img)


#kernel size is number of pixels in the kernel(number of rows and columns)
average = cv.blur(img,(3,3))  # Applying average filter with a 9x9 kernel
cv.imshow('average',average)

#Gaussian Blur

gauss = cv.GaussianBlur(img,(3,3),0)
cv.imshow('Gaussian Blur',gauss)

#Median Blur
# Median Blur is a non-linear filter that is effective in removing salt-and-pepper noise
#It replaces each pixel with the median of the pixels in the kernel

median = cv.medianBlur(img,3)
cv.imshow('Median Blur',median)

#Bilateral 
# Bilateral filter is effective in noise reduction while preserving edges

bilateral = cv.bilateralFilter(img,5,95,85)
cv.imshow('Bilateral',bilateral)

#cvbilateral filter (img, diameter, sigmaColor, sigmaSpace)






cv.waitKey(0) 

# Convert the image to RGB format
