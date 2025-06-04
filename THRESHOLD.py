import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('PHOTOS/billu1.jpeg')
cv.imshow('cute',img)

#Simple Thresholding

# 📌 Thresholding in OpenCV (Hinglish Explanation)
# Image ko black & white mein convert karta hai
# Pixel > threshold → white (255)
# Pixel <= threshold → black (0)
# Use hota hai object/background alag karne ke liye
# Example: cv2.threshold(gray_img, 127, 255, cv2.THRESH_BINARY)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

threshold , thresh = cv.threshold(gray,30,255,cv.THRESH_BINARY)
cv.imshow('Simple thresholding',thresh)


threshold, thresh_inv = cv.threshold(gray,30,255,cv.THRESH_BINARY_INV)
cv.imshow('Simple thresholding Inverse',thresh_inv)

#Adaptive Thresholding 
adaptive_thresh = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,3)
cv.imshow('Adaptive Thresholding',adaptive_thresh)

adaptive_thresh = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.ADAPTIVE_THRESH_GAUSSIAN_C,11,3)
cv.imshow('Adaptive Thresholding',adaptive_thresh)
# -------------------------------
# 🔹 Simple Thresholding (Binary)
# Agar pixel > 30 ➡ 255 (white)
# Agar pixel <= 30 ➡ 0 (black)
# Ye fixed threshold pe based hota hai
threshold, thresh = cv.threshold(gray, 30, 255, cv.THRESH_BINARY)
cv.imshow('Simple thresholding', thresh)

# -------------------------------
# 🔹 Simple Thresholding (Binary Inverse)
# Agar pixel > 30 ➡ 0 (black)
# Agar pixel <= 30 ➡ 255 (white)
# Ye simple threshold ka ulta version hai
threshold, thresh_inv = cv.threshold(gray, 30, 255, cv.THRESH_BINARY_INV)
cv.imshow('Simple thresholding Inverse', thresh_inv)

# -------------------------------
# 🔹 Adaptive Thresholding (Mean)
# Har pixel ka threshold value apne 11x11 ke surrounding pixels ka average hota hai
# Us average me se 3 minus karke threshold decide hota hai
# Ye uneven lighting conditions ke liye best hota hai
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C,
                                       cv.THRESH_BINARY, 11, 3)
cv.imshow('Adaptive Thresholding', adaptive_thresh)

# Wait for keypress before closing windows
cv.waitKey(0)



 
