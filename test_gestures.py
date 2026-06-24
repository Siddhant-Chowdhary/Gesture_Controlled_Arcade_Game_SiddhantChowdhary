import cv2 as cv
import mediapipe as mp
import gestures 

def getLandmarkList(frame, handLandmarks):
    h, w, _ = frame.shape
    lmList = []
    for idx, lm in enumerate(handLandmarks.landmark):
        #To get coords from pixel ratios
        cx, cy = int(lm.x * w), int(lm.y * h)
        lmList.append([idx, cx, cy])
    return lmList

# Initialize MediaPipe Framework
mpHands = mp.solutions.hands
mpDraw = mp.solutions.drawing_utils
hands = mpHands.Hands( static_image_mode=False , max_num_hands=1 , min_detection_confidence=0.7 , min_tracking_confidence=0.5 )

# Camera selection if external or built in webcam to be used
print("-" * 30)
print("  Select camera")
print("-" * 30)
print("[0] for Built-in Laptop Webcam")
print("[1] External Webcam")
print("-" * 30)

cameraInput = input("Enter choice (0 or 1, default is 0): ").strip()
cameraIndex = 1 if cameraInput == "1" else 0
print(f"Connecting to camera index {cameraIndex}...")

cap = cv.VideoCapture(cameraIndex)

while True:
    success, frame = cap.read()
    if not success:
        break

    frame = cv.flip(frame, 1)  # Create mirror like environment
    rgb = cv.cvtColor(frame, cv.COLOR_BGR2RGB) #OpenCv and MediaPipe support different BGR and RGB
    results = hands.process(rgb)

    gesture = "NONE"

    if results.multi_hand_landmarks:
        # Extract landmarks for the primary hand
        handLandmarks = results.multi_hand_landmarks[0]
        
        # Pull real-time left or right hand classification
        handLabel = "Right"  
        if results.multi_handedness:
            handLabel = results.multi_handedness[0].classification[0].label

        # Visual updates
        mpDraw.draw_landmarks(frame, handLandmarks, mpHands.HAND_CONNECTIONS)
        lmList = getLandmarkList(frame, handLandmarks)

        if lmList:
            # Process geometry inside module using its exact handedness context
            gesture = gestures.classify(lmList, handLabel)
            
            # Print state array debugging strings cleanly to terminal
            current_fingers = gestures.fingersUp(lmList, handLabel)
            print(f"Hand: {handLabel:5} | Fingers: {current_fingers} | Output: {gesture}")

    cv.putText( frame , gesture , (20, 60) , cv.FONT_HERSHEY_SIMPLEX , 1.2 , (0, 255, 0) , 3 )

    cv.imshow('Test', frame)
    if cv.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv.destroyAllWindows()