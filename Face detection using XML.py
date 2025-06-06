import cv2 as cv
import os

img = cv.imread('PHOTOS/woman3.jpg')
if img is None:
    print("Failed to load image. Check the path: PHOTOS/woman3.jpg")
    exit()
cv.imshow('WOMAN', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

print(os.path.exists('haar_face.xml'))  # Should print True
haar_cascade = cv.CascadeClassifier('haar_face.xml')
if haar_cascade.empty():
    print("Failed to load haar_face.xml. The file may be missing or invalid.")
    exit()

faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=6)
print(f'Number of faces found = {len(faces_rect)}')

for (x, y, w, h) in faces_rect:
    cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), thickness=2)

cv.imshow('Detected faces', img)
cv.waitKey(0)
cv.destroyAllWindows()


