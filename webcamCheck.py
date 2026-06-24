import cv2 as cv

cap = cv.VideoCapture(0)

while True:
    success, img = cap.read()

    print(success)

    if not success:
        continue

    cv.imshow("Webcam Test", img)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()