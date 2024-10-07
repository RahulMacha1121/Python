import cv2
import mediapipe as mp

# Initialize Mediapipe hands module
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

# Initialize Mediapipe drawing module
mp_drawing = mp.solutions.drawing_utils

# Start video capture from the webcam
cap = cv2.VideoCapture(0)

def count_fingers(hand_landmarks):
    # Get the landmark positions
    landmarks = hand_landmarks.landmark
    
    # Define the tips of the fingers (using indices from Mediapipe)
    finger_tips = [mp_hands.HandLandmark.THUMB_TIP,
                   mp_hands.HandLandmark.INDEX_FINGER_TIP,
                   mp_hands.HandLandmark.MIDDLE_FINGER_TIP,
                   mp_hands.HandLandmark.RING_FINGER_TIP,
                   mp_hands.HandLandmark.PINKY_TIP]
    
    # Count the number of fingers that are up
    count = 0

    # Check if each finger is up
    for tip in finger_tips:
        # Check if the finger tip is above the MCP (metacarpophalangeal joint)
        if landmarks[tip].y < landmarks[tip - 2].y:
            count += 1

    return count

while True:
    success, image = cap.read()
    if not success:
        print("Ignoring empty camera frame.")
        continue

    # Convert the BGR image to RGB
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    # Process the image and find hands
    results = hands.process(image_rgb)

    # Initialize finger count
    finger_count = 0

    # Draw hand landmarks on the image
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Count fingers
            finger_count = count_fingers(hand_landmarks)

    # If no fingers are detected (all fingers closed), ensure it shows 0
    if finger_count == 0 and results.multi_hand_landmarks:
        finger_count = 0

    # Display the finger count
    cv2.putText(image, f'Fingers: {finger_count}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Display the image
    cv2.imshow("Finger Counting", image)

    # Break the loop when 'q' is pressed
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

# Release the webcam and destroy all OpenCV windows
cap.release()
cv2.destroyAllWindows()
