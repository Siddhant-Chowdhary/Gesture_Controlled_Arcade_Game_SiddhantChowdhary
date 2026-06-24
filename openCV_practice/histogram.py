import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('Screenshot (64).png')
cv.imshow('Cat' , img)

gray = cv.cvtColor(img , cv.COLOR_BGR2GRAY)
cv.imshow('Gray' , gray) 

#Grayscale histogram([0] is the index of channel)
gray_hist = cv.calcHist([gray] , [0] , None , [256] , [0,256] )

plt.figure()
plt.title('Gray Histogram')
plt.plot(gray_hist)
plt.xlim([0,256])
plt.show()

cv.waitKey(0)
