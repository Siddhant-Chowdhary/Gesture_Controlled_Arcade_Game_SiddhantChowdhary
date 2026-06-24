import math

def distance(lmList, p1, p2):
    #Calculates raw Euclidean distance
    x1, y1 = lmList[p1][1], lmList[p1][2]
    x2, y2 = lmList[p2][1], lmList[p2][2]
    return math.hypot(x2 - x1, y2 - y1)

def handScale(lmList):
    #Calculates a dynamic scale ratio based on hand-to-camera distance
    ref = distance(lmList, 0, 9)  # Wrist to middle finger knuckle
    return ref if ref != 0 else 1

def fingersUp(lmList, handLabel):
    #Returns [thumb, index, middle, ring, pinky], 1 = up
    fingers = []

    # New Rotation-Proof Thumb Logic
    # Compare distance from thumb tip (4) to pinky knuckle (17) 
    # vs. thumb inner joint (3) to pinky knuckle (17)
    tipToPinky = distance(lmList, 4, 17)
    jointToPinky = distance(lmList, 3, 17)

    # If the tip is pushed further away from the pinky side than the joint, it's UP
    fingers.append(1 if tipToPinky > jointToPinky else 0)

    # Thumb logic based on handedness label - compare x-coordinates
    #if handLabel == "Right":
    #   fingers.append(1 if lmList[4][1] > lmList[3][1] else 0)
    #else:
    #    fingers.append(1 if lmList[4][1] < lmList[3][1] else 0)

    #Other four fingers - compare y-coordinates ((0,0) is at top left end in OpenCv)
    for tip in [8, 12, 16, 20]:
        tipToWrist = distance(lmList, tip, 0)
        pipToWrist = distance(lmList, tip - 2, 0)  # pip is the middle joint
        
        # If the tip is further from the wrist than the middle joint, it is UP
        #Added to strenghten the PEACE and POINTING sign
        fingers.append(1 if tipToWrist > pipToWrist else 0) 

    return fingers

def classify(lmList, handLabel):
    #Main calculation which converts coordinates to gesture commands
    if not lmList or len(lmList) < 21:
        return "NONE"

    fingers = fingersUp(lmList, handLabel)
    scale = handScale(lmList)

    #Distance-based Gestures
    # Check normalized distance between thumb tip (4) and index tip (8)
    pinchDist = distance(lmList, 4, 8) / scale
    
    # An OK sign means thumb and index form a circle, while middle, ring, pinky point out
    if pinchDist < 0.3 and fingers[2] and fingers[3] and fingers[4]:
        return "OK"

    # Up and Down based Gestures
    if fingers == [0, 0, 0, 0, 0]:
        return "FIST"
    if fingers == [1, 1, 1, 1, 1]:
        return "OPEN PALM"
    #POINTING wasnt working when thumb got a bit free and went to right or left 
    if fingers == [0, 1, 0, 0, 0] or fingers == [1, 1, 0, 0, 0]:
        return "POINTING"
    if fingers == [0, 1, 1, 0, 0]:
        return "PEACE"
    if fingers == [1, 0, 0, 0, 0]:
        return "THUMBS UP"

    return "UNKNOWN"