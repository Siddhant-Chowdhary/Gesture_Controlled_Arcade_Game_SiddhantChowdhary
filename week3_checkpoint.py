import cv2
import mediapipe as mp


def get_landmark_list(frame, hand_landmarks):
    h, w, _ = frame.shape
    lm_list = []
    for idx, lm in enumerate(hand_landmarks.landmark):
        cx, cy = int(lm.x * w), int(lm.y * h)  #shows the pixels instead of values between 0 and 1
        lm_list.append([idx, cx, cy])
    return lm_list

def fingers_up(lm_list):
    """Returns a list of 5 ints [thumb, index, middle, ring, pinky], 1 = up."""
    tips = [4, 8, 12, 16, 20]
    fingers = []

    # Smart Thumb Logic: Compare horizontal distance to the index knuckle (Landmark 5)
    #To counter the problem where it wasnt showing palms up and couldn't differntiate between fist and thumbs up
    thumb_tip_dist = abs(lm_list[4][1] - lm_list[5][1])
    thumb_joint_dist = abs(lm_list[3][1] - lm_list[5][1])

    if thumb_tip_dist > thumb_joint_dist:
        fingers.append(1)
    else:
        fingers.append(0)

    # Other four fingers: compare y (tip above PIP joint = up)
    for tip in tips[1:]:
        fingers.append(1 if lm_list[tip][2] < lm_list[tip - 2][2] else 0)

    return fingers




def classify_gesture(fingers):
    if fingers == [0, 0, 0, 0, 0]:
        return "FIST"
    if fingers == [1, 1, 1, 1, 1]:
        return "OPEN PALM"
    if fingers == [0, 1, 0, 0, 0]:
        return "POINTING"
    if fingers == [0, 1, 1, 0, 0]:
        return "PEACE"
    if fingers == [1, 0, 0, 0, 0]:
        return "THUMBS UP"
    return "UNKNOWN"


mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,  
    min_detection_confidence=0.7,
    min_tracking_confidence=0.5,
)



#Getting the user to prompt if he wants external webcam or built-in laptop webcam
print("=" * 30)
print("  SELECT YOUR CAMERA SOURCE")
print("=" * 30)
print("[0] Built-in Laptop Webcam")
print("[1] External Webcam / USB Camera")
print("-" * 30)

camera_input = input("Enter choice (0 or 1, default is 0): ").strip()

# Validate input: if it's not '1', default safely to 0
if camera_input == "1":
    camera_index = 1
    print("Connecting to External Webcam...")
    print("If it fails to open, your system might have it assigned to index 2 or 0.")
else:
    camera_index = 0
    print("Connecting to Built-in Webcam...")

cap = cv2.VideoCapture(camera_index)




while True:
    success, frame = cap.read()
    if not success:
        break

    frame = cv2.flip(frame, 1)  # to feel natural
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # BGR -> RGB for MediaPipe
    results = hands.process(rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(
                frame, hand_landmarks, mp_hands.HAND_CONNECTIONS
            )
            lm_list = get_landmark_list(frame, hand_landmarks)

            
            if lm_list:
                fingers = fingers_up(lm_list)
                gesture = classify_gesture(fingers)

                print(f"Fingers State: {fingers} | Detected: {gesture}")

                # Text overlay
                cv2.putText(
                    frame,
                    gesture,
                    (20, 60),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1.2,
                    (0, 255, 0),
                    3,
                )

    cv2.imshow("Hand Tracking", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()