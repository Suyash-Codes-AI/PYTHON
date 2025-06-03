import cv2 as cv
import numpy as np

#Bitwise Operators
blank = np.zeros((400,400), dtype = 'uint8')
rectangle = cv.rectangle(blank.copy(),(30,30),(370,370),255,-1)
circle = cv.circle(blank.copy(),(200,200),200,255,-1)

cv.imshow('Rectangle',rectangle)
cv.imshow('Circle',circle)

#Bitwise AND

# This operation returns the pixels that are in both images.
# It is useful for masking operations where you want to keep only the overlapping areas.

bitwise_and = cv.bitwise_and(rectangle,circle)
cv.imshow('Bitwise AND', bitwise_and)

#BItiwise OR

# This operation returns the pixels that are in either of the images.

# It is useful for combining two images or shapes.
# It includes all pixels that are in either of the two images.
bitwise_or = cv.bitwise_or(rectangle, circle)
cv.imshow('bitwise_or',bitwise_or)

#Bitwise XOR
# This operation returns the pixels that are in either of the images but not in both.
# It is useful for highlighting the differences between two images or shapes.


btiwise_xor = cv.bitwise_xor(rectangle,circle)
cv.imshow('Bitwise XOR', btiwise_xor)


# Bitwise NOT
# This operation inverts the pixels of the image.   
bitwise_not_rectangle = cv.bitwise_not(rectangle)
cv.imshow('Bitwise Not Rectangle',bitwise_not_rectangle)

 
bitwise_not_circle = cv.bitwise_not(circle)
cv.imshow('Bitwise Not Circle', bitwise_not_circle) 
cv.waitKey(0) 


