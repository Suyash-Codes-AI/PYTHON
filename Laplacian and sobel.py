import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('PHOTOS/billu1.jpeg')
cv.imshow('cute',img)

#Canny edge is a popular edge detection algorithm and multi step process.
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)
#Laplacian
#Laplacian is a second order derivative operator that calculates the Laplacian of an image.
lap = cv.Laplacian(gray, cv.CV_64F)

lap = np.uint8(np.absolute(lap))
cv.imshow('Lapcian',lap)

# Laplacian operator apply kiya for edge detection (gray image par)
# Result ko absolute kiya aur uint8 banaya taaki image dikh sake
# Finally, 'Laplacian' naam ke window me image show kiya


#Sobel
#Sobel operator is used to find the gradient of the image intensity at each pixel.

# Sobel operator apply kiya for edge detection (gray image par).It find the gradient and detect edges in x and y direction.
sobelx = cv.Sobel(gray,cv.CV_64F,1,0)
sobely = cv.Sobel(gray,cv.CV_64F,0,1)

combined_sobel  = cv.bitwise_or(sobelx , sobely)


cv.imshow('Sobel x ',sobelx)
cv.imshow('Sobel y',sobely)
cv.imshow('combined sobel',combined_sobel)

# Apply Sobel operator to detect edges in the image.
# cv.Sobel() calculates the first-order derivative (gradient) of the image.
# This helps in identifying areas where the pixel intensity changes sharply — which are the edges.

# Parameters:
# - gray: Input image (must be in grayscale for edge detection).
# - cv.CV_64F: Output data type. 64-bit float allows for both positive and negative gradient values.
#              Using CV_8U (unsigned int) would clip negative gradients to 0, causing data loss.
# - dx and dy: Derivative orders in x and y directions:
#     - dx=1, dy=0: Finds the gradient in the x-direction (detects vertical edges).
#     - dx=0, dy=1: Finds the gradient in the y-direction (detects horizontal edges).
 

 
cv.waitKey(0) 

 
