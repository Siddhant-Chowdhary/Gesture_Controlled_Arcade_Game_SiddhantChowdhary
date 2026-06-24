import cv2 as cv
import numpy as np 
import time
import HandTrackingModule2 as htm
import math


from pycaw.pycaw import AudioUtilities
device = AudioUtilities.GetSpeakers()
volume = device.EndpointVolume
print(f"Audio output: {device.FriendlyName}")
#print(f"- Muted: {bool(volume.GetMute())}")
#print(f"- Volume level: {volume.GetMasterVolumeLevel()} dB")
#print(f"- Volume range: {volume.GetVolumeRange()[0]} dB - {volume.GetVolumeRange()[1]} dB")
#volume.SetMasterVolumeLevel(0.0, None)
volRange = volume.GetVolumeRange()
minVol = volRange[0]
maxVol = volRange[1]


wCam , hCam = 640 , 480

cap = cv.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
pTime = 0
cTime =0
vol = 0
volBar = 400

detector = htm.handDetector(detectionCon = 0.7)


while True:
    success , img = cap.read()

    img = detector.findHands(img)
    lmList = detector.findPosition(img , draw=False)
    if len(lmList)!=0:
        #print(lmList[4] , lmList[8])

        x1 ,y1 = lmList[4][1] , lmList[4][2]
        x2 ,y2 = lmList[8][1] , lmList[8][2] 
        cx , cy = (x1+x2)//2 , (y1+y2)//2

        cv.circle(img , (x1,y1) , 10 , (255,0,255) , cv.FILLED)
        cv.circle(img , (x2,y2) , 10 , (255,0,255) , cv.FILLED)
        cv.line(img ,(x1,y1) , (x2,y2) , (0,255,255) , 3 )
        cv.circle(img , (cx ,cy) , 10 , (0,255,0) , cv.FILLED)
        
        #Print dsitance between points
        length = math.hypot(x2-x1 , y2-y1)
        #print(length)

        #Hand Range is 50 to 300
        #Volume range is -65 to 0
        vol = np.interp(length , [50 , 300] , [minVol , maxVol])
        volBar = np.interp(length , [50 , 300] , [400,150])
        print(length , vol)
        volume.SetMasterVolumeLevel(vol, None)


        if length<=50:
            cv.circle(img , (cx ,cy) , 10 , (255,255,0) , cv.FILLED)

        cv.rectangle(img , (50 , 250) , (85,400) , (0,100,100) , 3)
        cv.rectangle(img , (50 , int(volBar)) , (85,400) , (100,100) , cv.FILLED)

    cTime = time.time()
    fps = 1 / (cTime-pTime)
    pTime =cTime

    cv.putText(img , f'FPS:{int(fps)}' , (40,70) , cv.FONT_HERSHEY_COMPLEX , 1, (255,0,0) , 2 )

    cv.imshow("Img" , img)
    cv.waitKey(1)

