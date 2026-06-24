import cv2 as cv

img =  cv.imread('Screenshot (64).png')

#differetn direct for live videos - capture.set(3,height)

def rescaleFrame(frame , scale=0.5):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)

    dimensions = (width , height)

    return cv.resize(frame , dimensions , interpolation = cv.INTER_AREA)

show = rescaleFrame(img)
cv.imshow('Cat' , show)

cv.waitKey(0)
