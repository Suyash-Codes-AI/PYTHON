import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('PHOTOS/billu1.jpeg')
cv.imshow('cute',img)


blank = np.zeros((img.shape[:2],img.shape[1]),dtype = 'unit8')

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

circle = cv.circle(blank,(img.shape[1]//2,img.shape[0]//2),100,255,-1)

mask = cv.bitwise_and(gray,gray,mask=circle)
cv.imshow('mask',mask)
#Grayscale histogram
"""
📷 Grayscale Histogram - In Short

A grayscale histogram shows how many pixels in an image 
have each brightness level from 0 (black) to 255 (white).

🛠️ Steps to Create It:
1. Convert image to grayscale.
2. Count pixels for each intensity (0–255).
3. Plot intensity vs frequency.

✅ Why It's Useful:
- Shows if an image is too dark or bright.
- Helps with contrast adjustment and image analysis.
"""


#Histogram is a graphical representation of the distribution of pixel intensities in an image.It is a list.Hist(gray, [256], [0, 256])

#In a histogram, a bin is a range of intensity values that are grouped together to count how many pixels fall into that range.'


gray_hist = cv.calcHist([gray], [0] , circle , [256],[0,256])
plt.figure()
plt.title('Grayscale Histogram')
plt.xlabel('Bins')
plt.ylabel('Number of pixels')
plt.plot(gray_hist)
plt.xlim([0,256])

plt.show()


#Colour Histogram

plt.figure()
plt.title('grayscale Histogram')
plt.xlabel('Bins')
plt.ylabel('No of pixels in the image ')


colors = ('b','g','r')
for i,col in enumerate(colors):
    hist = cv.calcHist([img],[i],None,[256],[0,256])
    plt.plot(hist,color=col)
    plt.xlim([0,256])
    plt.title('color histogram')
plt.show() 


cv.waitKey(0) 

 
