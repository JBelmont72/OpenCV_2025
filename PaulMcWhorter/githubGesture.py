import cv2
import numpy as np

from mediapipe import Image, ImageFormat
from mediapipe.tasks.python.vision import HandLandmarker, HandLandmarkerOptions, RunningMode
from mediapipe.tasks.python import BaseOptions
from mediapipe import solutions
from mediapipe.framework.formats import landmark_pb2


def draw_landmarks_on_image(rgb_image, detection_result):
  hand_landmarks_list = detection_result.hand_landmarks
  annotated_image = np.copy(rgb_image)

  # Loop through the detected hands to visualize.
  for idx in range(len(hand_landmarks_list)):
    hand_landmarks = hand_landmarks_list[idx]

    # Draw the hand landmarks.
    hand_landmarks_proto = landmark_pb2.NormalizedLandmarkList()
    hand_landmarks_proto.landmark.extend([
      landmark_pb2.NormalizedLandmark(x=landmark.x, y=landmark.y, z=landmark.z) for landmark in hand_landmarks
    ])
    solutions.drawing_utils.draw_landmarks(
      annotated_image,
      hand_landmarks_proto,
      solutions.hands.HAND_CONNECTIONS,
      solutions.drawing_styles.get_default_hand_landmarks_style(),
      solutions.drawing_styles.get_default_hand_connections_style())

  return annotated_image


# Options for the hand landmarker
base_options = BaseOptions(model_asset_path='hand_landmarker.task')  # Ensure this path is correct and points to a .tflite file
options = HandLandmarkerOptions(
    base_options=base_options,
    num_hands=2,
    min_hand_detection_confidence=0.1,
    min_tracking_confidence=0.1,
    running_mode=RunningMode.IMAGE
)
detector = HandLandmarker.create_from_options(options)

# Setup camera capture
cap = cv2.VideoCapture(1)

if not cap.isOpened():
    print("Failed to open capture device")
    exit(1)

# Run inference on the video
print("Running hand landmarker...")

while True:
    success, frame = cap.read()

    if not success:
        break

    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame using HandLandmarker
    mp_image = Image(image_format=ImageFormat.SRGB, data=rgb_frame)
    results = detector.detect(mp_image)

    # Draw the hand landmarks on the frame
    if results:
        annotated_image = draw_landmarks_on_image(mp_image.numpy_view(), results)
        bgr_frame = cv2.cvtColor(annotated_image, cv2.COLOR_RGB2BGR)
        cv2.imshow("Frame", bgr_frame)

    if cv2.waitKey(1) & 0xFF == 27:  # Exit on ESC
        break

cap.release()
cv2.destroyAllWindows()