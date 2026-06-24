# Gesture_Controlled_Arcade_Game_SiddhantChowdhary
A gesture-controlled game built with Python, OpenCV, MediaPipe, and Pygame. The player controls the game entirely through hand gestures captured by a standard webcam.


## Project Architecture

To ensure clean code and easy integration with future game engines, the project is strictly divided into two main components:

### 1. gestures.py
This is a standalone module that handles all the complex 2D geometry. It contains no webcam or drawing logic. Instead of relying on absolute X/Y coordinates (which break when the hand tilts or moves away from the camera), it uses **normalized Euclidean distances**. 
* **Scale-Invariant:** Gestures work whether your hand is 1 foot or 3 feet away from the lens.
* **Rotation-Proof:** Uses structural anchors (like measuring the thumb tip to the pinky knuckle) so gestures like "Thumbs Up" work even if the hand is rotated.
* **Main API:** Exposes a single `classify(lm_list, hand_label)` function that takes landmark data and returns a gesture string.

### 2. test_gestures.py (The Visual Frontend)
This is the testing harness and webcam loop. It handles:
* Capturing the live video feed via OpenCV.
* Passing the RGB frames to the MediaPipe hands model.
* Extracting the 21 hand landmarks and passing them to `gestures.py`.
* Drawing the skeletal overlay and the live gesture text HUD onto the screen.

### 📁 `opencv_practice/`
*Contains smaller scripts and foundational exercises built while learning the basics of computer vision and the OpenCV library.*

## ✋ Supported Gestures

The engine currently recognizes 6 distinct states reliably:
* **FIST:** All fingers folded tightly.
* **OPEN PALM:** All five fingers fully extended.
* **POINTING:** Index finger extended, others folded (supports both tucked and relaxed thumb).
* **PEACE:** Index and middle fingers extended.
* **THUMBS UP:** Thumb extended outward, other fingers folded tightly.
* **OK SIGN:** Thumb and index finger pinched together, remaining fingers extended (calculated via normalized pinch distance).

## 🛠️ How to Run

1. Clone the repository.
2. Install the required dependencies:
   ```bash
   pip install opencv-python mediapipe
