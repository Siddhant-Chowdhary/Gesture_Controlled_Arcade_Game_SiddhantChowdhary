import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3) , dtype = 'uint8')
cv.imshow('Blank' ,blank)

blank[200:300 , 400:500] = 0,255,0
cv.imshow('Red' ,blank)

#blank[:] = 0,255,0
#cv.imshow('Green' ,blank)

#CIRCLE(bg image, center, radius , color)
cv.circle(blank , (blank.shape[1]//2, blank.shape[0]//2) ,  40 , (0,0,255))
cv.imshow('Circle',blank)

#RECTANGLE cv.rectangle(blank , (blank.shape[1]//2, blank.shape[0]//2) ,  40 , (0,0,255))
#LINE cv.line

img =  cv.imread('Screenshot (64).png')
cv.imshow('Cat' , img)

cv.waitKey(0)