import cv2 as cv

img = cv.imread('Screenshot (64).png')

cv.imshow('Cat' , img)

#1. Converting to GRAYSCALE
gray = cv.cvtColor(img , cv.COLOR_BGR2GRAY)
cv.imshow('Gray' , gray)

#2. BLUR
blur = cv.GaussianBlur(img , (3,3) , cv.BORDER_DEFAULT)
cv.imshow('Blur' , blur)

#3.COSCODE-highlights the edges 
canny = cv.Canny(img , 150 , 175)
cv.imshow('Canny' , canny)

#4. Dilating  - cv,dilating - thickens the edges 

#5. ERODING - cv,erode(dilate , (3,3) , iterations = 5)

#RESIZE
r = cv.resize(img , (300,300))
cv.imshow('r' , r)

#CROPPED
#cropped = img(150:100)
#cv.imshow


cv.waitKey(0)
