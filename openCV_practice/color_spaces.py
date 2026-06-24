import cv2 as cv

img =  cv.imread('Screenshot (64).png')
cv.imshow('Cat' , img)

gray = cv.cvtColor(img , cv.COLOR_BGR2GRAY)
cv.imshow('Gray' , gray)

#HSV
hsv = cv.cvtColor(img , cv.COLOR_BGR2HSV)
cv.imshow('HSV' , hsv)

#LAB
lab = cv.cvtColor(img , cv.COLOR_BGR2LAB)
cv.imshow('Lab' , lab)


cv.waitKey(0)