import cv2 as cv
import numpy as np
img = cv.imread('PHOTOS/cat.jpg')
#Traslation of the image 

def Translate(img,x,y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1],img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

translated = Translate(img, 84, 120)
cv.imshow('Translated Image', translated)

# Rotate the imgae 

def rotate(img,angle,rotPoint = None):
    (height,width) = img.shape[:2]
    if rotPoint is None:
        rotPoint = (width//2,height//2)
        rotMat = cv.getRotationMatrix2D(rotPoint,angle,1.0)
        dimensions = (width,height)
        return cv.warpAffine(img,rotMat,dimensions)
    rotated = rotate(img,45)
    cv.imshow('Rotated Image', rotated)

# Resize the image  

resized = cv.resize(img,(520,98660),interpolation = cv.INTER_CUBIC)
cv.imshow('resized image',resized)
 
#Flipping the imaage 
flip = cv.flip(img,0)  # 1 for horizontal flip
cv.imshow('Flipped Image', flip)

#0 for vertical flip
#-1 for both horizontal and vertical flip


#cRopping the image 
cropped = img[50:200, 100:300]  # y1:y2, x1:x2
cv.imshow('Cropped Image', cropped)

cv.waitKey(0)  # Wait for a key press to close the window
