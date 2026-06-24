import cv2 as cv

#img =  cv.imread('Screenshot (64).png')

#cv.imshow('Cat' , img)



#cv.waitKey(0)

#Reading videos
capture = cv.VideoCapture('')_

while (true):
    isTrue, frame = capture.read()

    cv.imshow('Video' , frame)

    if cv.WaitKey(20) &0xFF==ord('d'):
        break

capture.release()
cv.destroyAllwindows