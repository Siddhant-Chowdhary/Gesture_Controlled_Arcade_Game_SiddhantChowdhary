import cv2 as cv
import numpy as np

#img = cv.imread('Roger.jpg')
img = cv.imread('big4.jpg')
cv.imshow('big4' , img)

gray = cv.cvtColor(img , cv.COLOR_BGR2GRAY)
cv.imshow('Gray' , gray)

haar_cascade = cv.CascadeClassifier('haar_face.xml')

faces_rect = haar_cascade.detectMultiScale(gray , scaleFactor = 1.05 , minNeighbors = 3)

print(f'Number of faces are = {len(faces_rect)}')
for (x,y,w,h) in faces_rect:
    cv.rectangle(img , (x,y) , (x+w,y+h) , (0,255,0) , thickness=2)

cv.imshow('Detected' , img)

cv.waitKey(0)