import cv2
import numpy as np
import pyautogui


# Load Haar Cascade Classifier for eyes
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

def calculate_new_mouse_position(gaze_direction):
    # Implement your logic to map gaze direction to mouse position
    # This is a placeholder, and you may need more advanced methods for accurate mapping
    return gaze_direction

cap = cv2.VideoCapture(0)  # 0 represents the default camera

while True:
    ret, frame = cap.read()

    # Perform any pre-processing here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Detect eyes in the frame
    eyes = eye_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Iterate through detected eyes
    for (ex, ey, ew, eh) in eyes:
        # Draw a rectangle around each eye
        cv2.rectangle(frame, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

        # Extract the region of interest (ROI) for each eye
        roi_eye = frame[ey:ey + eh, ex:ex + ew]

        # Implement further processing on the eye region if needed

        # Example: Calculate the new mouse position based on gaze direction
        new_mouse_position = calculate_new_mouse_position((ex + ew // 2, ey + eh // 2))

        # Move the mouse
        pyautogui.moveTo(new_mouse_position[0], new_mouse_position[1])
    cv2.imshow('Eye Tracking', frame)

    if cv2.waitKey(1) & 0xFF == 27:  # Press 'Esc' to exit
        break

cap.release()
cv2.destroyAllWindows()
