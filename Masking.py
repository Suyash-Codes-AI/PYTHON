import cv2 as cv
import numpy as np

img = cv.imread('PHOTOS/billu1.jpeg')
cv.imshow('cute',img)

blank = np.zeros(img.shape[:2], dtype = 'uint8')
cv.imshow('Blank',blank)

#circular mask. We can also use rectanuglr mask or any other shape.



mask  = cv.circle(blank, (img.shape[1]//2,img.shape[0]//2),100, 255,-1)

#we can also use cv.rectangle() for rectangular mask

#weird shape mask
maskweird = cv.fillPoly(blank, pts = [np.array([[100,100],[200,100],[200,200],[100,200]], np.int32)], color = 255)

cv.imshow('mask',maskweird)



masked = cv.bitwise_and(img,img,mask = mask)
cv.imshow('masked image',masked)
cv.imshow('MASK',mask)
cv.waitKey(0) 

 
