import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('Screenshot (64).png')
cv.imshow('Cat' , img)

gray = cv.cvtColor(img , cv.COLOR_BGR2GRAY)
cv.imshow('Gray' , gray)

#Simple  thresholding(threshold is the value 150 while thresh is the image)
threshold , thresh = cv.threshold(gray , 150 , 255, cv.THRESH_BINARY)
cv.imshow('Thresh' , thresh)

threshold , thresh_inv = cv.threshold(gray , 150 , 255 , cv.THRESH_BINARY_INV)
cv.imshow('Thresh Inversed' , thresh_inv)

#Adoptive thresholding = find threshold value itself(block size and 3 is the value we want to ereduce from the mean which is of 11 blocks)
adaptive_thresh = cv.adaptiveThreshold(gray , 255 , cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY , 11, 3 )
cv.imshow('Adaptive' , adaptive_thresh )

cv.waitKey(0) 