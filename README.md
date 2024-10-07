# Computer Vision Projects with OpenCV and Mediapipe

This repository contains a collection of Python scripts that perform various real-time computer vision tasks such as face detection, finger counting, and hand tracking. These projects utilize OpenCV and Mediapipe libraries to process video streams from the webcam, detect faces, hands, and fingers, and visually display the results.

## Project Descriptions

### 1. Face Detection (`face_detection.py`)

This script performs real-time face detection using the **Haar Cascade Classifier**. It captures video from the webcam, converts each frame to grayscale, and uses a pre-trained model (`haarcascade_frontalface_default.xml`) to detect faces. Detected faces are highlighted by drawing rectangles around them in the live video feed.

- **Technology**: OpenCV, Haar Cascade
- **Use Case**: Basic face detection for security systems, camera apps, etc.

### 2. Finger Counting (`finger_counting.py`)

This script tracks the user's hand in real-time and counts how many fingers are raised. It uses **Mediapipe**'s hand tracking module to detect the hand's position and landmarks. Based on these landmarks, the script determines which fingers are raised and displays the count in the video frame.

- **Technology**: Mediapipe, OpenCV
- **Use Case**: Gesture recognition, touchless interfaces, or hand-based controls.

### 3. Hand Tracking (`hand_tracking.py`)

This script uses **Mediapipe**'s hand tracking module to detect and track the movement of the user's hand in real-time. It draws landmarks on the hand to show each joint and finger position, providing a visual representation of the hand's structure and movements.

- **Technology**: Mediapipe, OpenCV
- **Use Case**: Motion tracking, gesture analysis, and hand gesture-controlled applications.

## Features

- **Real-Time Face Detection**: Detects human faces from the webcam feed using the pre-trained Haar Cascade model.
- **Finger Counting**: Counts the number of raised fingers based on hand tracking.
- **Hand Tracking**: Visualizes hand landmarks to track finger and hand movements.
  
## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/computer-vision-projects.git
   cd computer-vision-projects
