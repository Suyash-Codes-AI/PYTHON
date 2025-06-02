import cv2 as cv
import numpy as np

# Read the image

img = cv.imread('PHOTOS/billu1.jpeg')
cv.imshow('billu1',img)

blank = np.zeros(img.shape[:2],dtype='uint8')
# Create a blank image with the same shape as the original image



b,g,r = cv.split(img)
blue = cv.merge([b,blank,blank])  # Create a blue channel image
green = cv.merge([blank,g,blank])  # Create a green channel image
red = cv.merge([blank,blank,r])  # Create a red channel image
cv.imshow('Blue Channel',blue)
cv.imshow('Green Channel',green)
cv.imshow('Red Channel',red)



# Split the image into its blue, green, and red channels
cv.imshow('Blue',b)
cv.imshow('Green',g)
cv.imshow('Red',r)

print(img.shape)  # Print the shape of the image
print(b.shape)  # Print the shape of the blue channel
print(g.shape)  # Print the shape of the green channel
print(r.shape) # Print the shape of the red channel

merged = cv.merge((b,g,r))
cv.imshow('Merged Image',merged)



cv.waitKey(0) 

# Convert the image to RGB format
