# Eye Tracking

The Eye Tracking script uses OpenCV and PyAutoGUI to track a user's eye movements and translates them into mouse movements on the screen. By leveraging the Haar Cascade Classifier for eyes, it detects the user's gaze direction and maps it to the cursor position. This project is a basic implementation and serves as a foundation for more complex eye-tracking applications.

## Prerequisites

Before you start using the Eye Tracking script, ensure you have Python installed on your system. Additionally, you will need to install the following Python libraries:

- OpenCV (cv2)
- NumPy
- PyAutoGUI

## Installation

1. Clone this repository to your local machine or download the files directly.

2. Navigate to the project directory and install the required Python libraries by running:

```bash
pip install opencv-python numpy pyautogui
```

Download the haarcascade_frontalface_default.xml and haarcascade_eye.xml Haar Cascade files from the OpenCV repository or any other source you trust. Place these files in the project directory.

## Usage
To start the Eye Tracking script, execute the following command in your terminal:

```bash
python eye_tracking.py
```

Ensure your face is visible to the camera, and the script will begin tracking your eye movements to control the mouse cursor. The script displays a live feed from your camera with rectangles drawn around detected eyes.

Press the 'Esc' key to exit the script.

## Customization
The script includes a placeholder function, calculate_new_mouse_position, which you can modify to improve the accuracy of gaze direction to mouse position mapping. Advanced mapping techniques may require additional logic and calibration for effective use.

## Notes
This script is a proof of concept and may require adjustments for optimal performance in different environments or lighting conditions.
Eye tracking accuracy and responsiveness can vary based on the camera quality and the user's distance from the camera.

## License
This project is open-sourced
