'''https://youtu.be/UcOxIepgFbQ
we describe what our approach will be to creating a gesture detection and recognition algorithm using mediaPipe. We will demonstrate the algorithm with some simple code demos. In future lessons we will further develop the algorithm.  
https://youtu.be/5TBROIHpdxQ


'''

#########~~~~~~~~~~~~~~~~~

# import cv2
# import numpy as np

# print(cv2.__version__)

# # Mediapipe wrapper
# class mpHands:
#     import mediapipe as mp
#     def __init__(self, maxHands=2, tol1=.5, tol2=.5):
#         self.width = 1280
#         self.height = 720
#         self.hands = self.mp.solutions.hands.Hands(
#             static_image_mode=False,
#             max_num_hands=maxHands,
#             min_detection_confidence=tol1,
#             min_tracking_confidence=tol2
#         )

#     def Marks(self, frame):
#         myHands = []
#         frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#         results = self.hands.process(frameRGB)
#         if results.multi_hand_landmarks is not None:
#             for handLandMarks in results.multi_hand_landmarks:
#                 myHand = []
#                 for landMark in handLandMarks.landmark:
#                     myHand.append((
#                         int(landMark.x * self.width),
#                         int(landMark.y * self.height)
#                     ))
#                 myHands.append(myHand)
#         return myHands

# # Distance between all points
# def findDistances(handData):
#     distMatrix = np.zeros([len(handData), len(handData)], dtype='float')
#     for row in range(len(handData)):
#         for col in range(len(handData)):
#             distMatrix[row][col] = np.linalg.norm(np.array(handData[row]) - np.array(handData[col]))
#     return distMatrix

# # Error comparison
# def findError(gestureMatrix, unknownMatrix, keyPoints):
#     error = 0
#     for row in keyPoints:
#         for col in keyPoints:
#             error += abs(gestureMatrix[row][col] - unknownMatrix[row][col])
#     return error


# # === MAIN PROGRAM ===

# cam = cv2.VideoCapture(1)
# cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
# cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
# cam.set(cv2.CAP_PROP_FPS, 30)
# cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

# findHands = mpHands(1)
# keyPoints = [0, 4, 5, 9, 13, 17, 8, 12, 16, 20]

# train = True
# trained = False

# print("Show your gesture and press 't' to train.")

# while True:
#     ret, frame = cam.read()
#     frame = cv2.resize(frame, (1280, 720))
#     handData = findHands.Marks(frame)

#     key = cv2.waitKey(1) & 0xFF

#     if train and handData != []:
#         if key == ord('t'):
#             knownGesture = findDistances(handData[0])  # Use only first hand
#             train = False
#             trained = True
#             print("Gesture trained! Move your hand to test recognition.")

#     if trained and handData != []:
#         unknownGesture = findDistances(handData[0])
#         error = findError(knownGesture, unknownGesture, keyPoints)
#         text = f"Error: {int(error)}"
#         cv2.putText(frame, text, (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 4)

#     # Draw keypoints
#     for hand in handData:
#         for ind in keyPoints:
#             cv2.circle(frame, hand[ind], 15, (255, 0, 255), -1)

#     cv2.imshow('my WEBcam', frame)
#     cv2.moveWindow('my WEBcam', 0, 0)

#     if key == ord('q'):
#         break

# cam.release()
# cv2.destroyAllWindows()
#####~~~~~~~~~~
# import cv2
# import numpy as np

# print(cv2.__version__)

# class mpHands:
#     import mediapipe as mp
#     def __init__(self, maxHands=2, tol1=.5, tol2=.5):
#         self.width = 1280
#         self.height = 720
#         self.hands = self.mp.solutions.hands.Hands(
#             static_image_mode=False,
#             max_num_hands=maxHands,
#             min_detection_confidence=tol1,
#             min_tracking_confidence=tol2
#         )

#     def Marks(self, frame):
#         myHands = []
#         frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#         results = self.hands.process(frameRGB)
#         if results.multi_hand_landmarks is not None:
#             for handLandMarks in results.multi_hand_landmarks:
#                 myHand = []
#                 for landMark in handLandMarks.landmark:
#                     myHand.append((
#                         int(landMark.x * self.width),
#                         int(landMark.y * self.height)
#                     ))
#                 myHands.append(myHand)
#         return myHands

# def findDistances(handData):
#     distMatrix = np.zeros([len(handData), len(handData)], dtype='float')
#     for row in range(len(handData)):
#         for col in range(len(handData)):
#             distMatrix[row][col] = np.linalg.norm(
#                 np.array(handData[row]) - np.array(handData[col]))
#     return distMatrix

# def findError(gestureMatrix, unknownMatrix, keyPoints):
#     error = 0
#     for row in keyPoints:
#         for col in keyPoints:
#             error += abs(gestureMatrix[row][col] - unknownMatrix[row][col])
#     return error

# # === MAIN CODE ===
# cam = cv2.VideoCapture(1)
# cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
# cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
# cam.set(cv2.CAP_PROP_FPS, 30)
# cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

# findHands = mpHands(1)
# keyPoints = [0, 4, 5, 9, 13, 17, 8, 12, 16, 20]

# train = True
# trained = False

# print("Show your gesture and press 't' to train.")

# while True:
#     ret, frame = cam.read()
#     frame = cv2.resize(frame, (1280, 720))
#     handData = findHands.Marks(frame)

#     # Draw keypoints
#     for hand in handData:
#         for ind in keyPoints:
#             cv2.circle(frame, hand[ind], 15, (255, 0, 255), -1)

#     # Show frame
#     cv2.imshow('my WEBcam', frame)
#     key = cv2.waitKey(1) & 0xFF  # ONLY ONE CALL

#     # Handle quit
#     if key == ord('q'):
#         break

#     # Handle training
#     if train and key == ord('t') and handData:
#         knownGesture = findDistances(handData[0])
#         print("Gesture trained!")
#         train = False
#         trained = True

#     # If trained, compute and show error
#     if trained and handData:
#         unknownGesture = findDistances(handData[0])
#         error = findError(knownGesture, unknownGesture, keyPoints)
#         cv2.putText(frame, f'Error: {int(error)}', (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 4)

# cam.release()
# cv2.destroyAllWindows()
#########~~~~~~~~~!!!!!!!!!!!!!  first PyQt5 version trains and reports errors
# import sys
# import cv2
# import numpy as np
# from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget
# from PyQt5.QtGui import QImage, QPixmap
# from PyQt5.QtCore import QTimer
# import mediapipe as mp

# class HandGestureTrainer(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Hand Gesture Trainer")
#         self.setFixedSize(1200, 700)  # Adjust window size
#         self.image_label = QLabel()
#         self.image_label.setFixedSize(1200, 680)  # Size for webcam display

#         self.train_button = QPushButton("Train Gesture")
#         self.train_button.setFixedHeight(40)  # Optional: make button height consistent
#         self.train_button.clicked.connect(self.train_gesture)


#         layout = QVBoxLayout()
#         layout.addWidget(self.image_label)
#         layout.addWidget(self.train_button)
#         self.setLayout(layout)

#         self.cap = cv2.VideoCapture(1)
#         self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
#         self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

#         self.mp_hands = mp.solutions.hands.Hands(static_image_mode=False, max_num_hands=1)
#         self.keyPoints = [0, 4, 5, 9, 13, 17, 8, 12, 16, 20]
#         self.knownGesture = None

#         self.timer = QTimer()
#         self.timer.timeout.connect(self.update_frame)
#         self.timer.start(30)

#     def train_gesture(self):
#         if hasattr(self, 'last_hand') and self.last_hand is not None:
#             self.knownGesture = self.find_distances(self.last_hand)
#             print("Gesture trained!")

#     def update_frame(self):
#         ret, frame = self.cap.read()
#         frame = cv2.flip(frame, 1)  # Flip for mirror view
#         handData = self.get_hand_landmarks(frame)

#         if handData:
#             self.last_hand = handData[0]  # Store for training
#             for ind in self.keyPoints:
#                 cv2.circle(frame, handData[0][ind], 15, (255, 0, 255), -1)

#             if self.knownGesture is not None:
#                 unknownGesture = self.find_distances(handData[0])
#                 error = self.find_error(self.knownGesture, unknownGesture)
#                 cv2.putText(frame, f'Error: {int(error)}', (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 4)

#         # Convert to Qt format
#         rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#         h, w, ch = rgb_image.shape
#         bytes_per_line = ch * w
#         qt_image = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format_RGB888)
#         self.image_label.setPixmap(QPixmap.fromImage(qt_image))

#     def get_hand_landmarks(self, frame):
#         frame = cv2.resize(frame, (1200, 680))

#         frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#         results = self.mp_hands.process(frame_rgb)
#         if results.multi_hand_landmarks:
#             landmarks = []
#             for lm in results.multi_hand_landmarks[0].landmark:
#                 x = int(lm.x * 1280)
#                 y = int(lm.y * 720)
#                 landmarks.append((x, y))
#             return [landmarks]
#         return []

#     def find_distances(self, handData):
#         distMatrix = np.zeros([len(handData), len(handData)], dtype='float')
#         for row in range(len(handData)):
#             for col in range(len(handData)):
#                 distMatrix[row][col] = np.linalg.norm(
#                     np.array(handData[row]) - np.array(handData[col]))
#         return distMatrix

#     def find_error(self, gestureMatrix, unknownMatrix):
#         error = 0
#         for row in self.keyPoints:
#             for col in self.keyPoints:
#                 error += abs(gestureMatrix[row][col] - unknownMatrix[row][col])
#         return error

#     def closeEvent(self, event):
#         self.cap.release()
#         super().closeEvent(event)

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = HandGestureTrainer()
#     window.show()
#     sys.exit(app.exec_())
############## next version is to get multiple hand positions

import sys
import cv2
import numpy as np
import pickle
from PyQt5.QtWidgets import (
    QApplication, QLabel, QPushButton, QVBoxLayout,
    QWidget, QLineEdit, QHBoxLayout
)
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import QTimer
import mediapipe as mp


class HandGestureTrainer(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hand Gesture Trainer")
        self.setFixedSize(1200, 700)

        self.image_label = QLabel()
        self.image_label.setFixedSize(1200, 680)

        self.label_input = QLineEdit()
        self.label_input.setPlaceholderText("Enter gesture label")

        self.train_button = QPushButton("Train Gesture")
        self.train_button.setFixedHeight(40)
        self.train_button.clicked.connect(self.train_gesture)

        h_layout = QHBoxLayout()
        h_layout.addWidget(self.label_input)
        h_layout.addWidget(self.train_button)

        layout = QVBoxLayout()
        layout.addWidget(self.image_label)
        layout.addLayout(h_layout)
        self.setLayout(layout)

        self.cap = cv2.VideoCapture(0)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

        self.mp_hands = mp.solutions.hands.Hands(static_image_mode=False, max_num_hands=1)
        self.keyPoints = [0, 4, 5, 9, 13, 17, 8, 12, 16, 20]
        self.knownGesture = None
        self.last_hand = None

        try:
            with open('gestures.pkl', 'rb') as f:
                self.gesture_library = pickle.load(f)
                print("Loaded saved gestures.")
        except FileNotFoundError:
            self.gesture_library = {}

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(30)

    def train_gesture(self):
        label = self.label_input.text().strip()
        if not label:
            print("Please enter a label for this gesture.")
            return

        if self.last_hand is not None:
            distances = self.find_distances(self.last_hand)
            self.gesture_library[label] = distances
            print(f"Gesture '{label}' trained and stored.")
            self.label_input.clear()

            with open('gestures.pkl', 'wb') as f:
                pickle.dump(self.gesture_library, f)
                print("Saved gestures to file.")

    def update_frame(self):
        ret, frame = self.cap.read()
        frame = cv2.flip(frame, 1)
        handData = self.get_hand_landmarks(frame)

        if handData:
            self.last_hand = handData[0]
            for ind in self.keyPoints:
                cv2.circle(frame, handData[0][ind], 15, (255, 0, 255), -1)

            unknownGesture = self.find_distances(handData[0])

            if self.gesture_library:
                errors = {}
                for label, gesture_matrix in self.gesture_library.items():
                    error = self.find_error(gesture_matrix, unknownGesture)
                    errors[label] = error

                best_match = min(errors, key=errors.get)
                cv2.putText(frame, f'Match: {best_match}', (50, 160),
                            cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 255), 4)

        rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        qt_image = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format_RGB888)
        self.image_label.setPixmap(QPixmap.fromImage(qt_image))

    def get_hand_landmarks(self, frame):
        frame = cv2.resize(frame, (1200, 680))
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.mp_hands.process(frame_rgb)
        if results.multi_hand_landmarks:
            landmarks = []
            for lm in results.multi_hand_landmarks[0].landmark:
                x = int(lm.x * 1280)
                y = int(lm.y * 720)
                landmarks.append((x, y))
            return [landmarks]
        return []

    def find_distances(self, handData):
        distMatrix = np.zeros([len(handData), len(handData)], dtype='float')
        for row in range(len(handData)):
            for col in range(len(handData)):
                distMatrix[row][col] = np.linalg.norm(
                    np.array(handData[row]) - np.array(handData[col]))
        return distMatrix

    def find_error(self, gestureMatrix, unknownMatrix):
        error = 0
        for row in self.keyPoints:
            for col in self.keyPoints:
                error += abs(gestureMatrix[row][col] - unknownMatrix[row][col])
        return error

    def closeEvent(self, event):
        self.cap.release()
        with open('gestures.pkl', 'wb') as f:
            pickle.dump(self.gesture_library, f)
        super().closeEvent(event)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = HandGestureTrainer()
    window.show()
    sys.exit(app.exec_())
