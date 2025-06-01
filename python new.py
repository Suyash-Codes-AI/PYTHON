import cv2 as cv
import numpy as np
blank = np.zeros((500,500,3 ),dtype='uint8')
cv.imshow('Blank',blank) 
 # Display the blank image
cv.rectangle(blank,(0,0),(250,500),(255,0,0),thickness = 2)
# Draw a rectangle on the blank image
cv.imshow('Recntagle',blank)
cv.circle(blank,(250,250),90,(0,255,0),thickness =-1)
cv.imshow('circle',blank)
# Draw a circle on the blank image
cv.putText(blank,'open cv',(225,225),cv.FONT_HERSHEY_TRIPLEX,1,(0,255,255),2)

cv.imshow('Text',blank)
# Draw text on the blank image
cv.line(blank,(-70,90),(250,250),(0,0,255),thickness=3)
cv.imshow('line',blank)
# Load an image from file and display it

img = cv.imread('PHOTOS/cat.jpg')
cv.imshow('Cat',img)

#gray scale conversion
gray = cv.cvtColor(img,cv.COLOR_BAYER_BG2BGRAY)
cv.imshow('Gray',gray)
cv.waitKey(0)  # Wait for a key press to close the window
cv.destroyAllWindows()  # Close all OpenCV windows