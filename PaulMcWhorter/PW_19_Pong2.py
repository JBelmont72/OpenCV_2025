'''
two handed pong with a cap set for speed

'''
import cv2
import sys
import mediapipe as mp

class mpHands:
    def __init__(self, maxHands=2):
        self.hands = mp.solutions.hands.Hands(static_image_mode=False, max_num_hands=maxHands, 
                                              min_detection_confidence=0.5, min_tracking_confidence=0.5)

    def Marks(self, frame):
        myHands, myHandTypes = [], []
        frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.hands.process(frameRGB)
        if results.multi_hand_landmarks:
            for handLandMarks in results.multi_hand_landmarks:
                myHand = [(int(landMark.x * width), int(landMark.y * height)) for landMark in handLandMarks.landmark]
                myHands.append(myHand)
            for hand in results.multi_handedness:
                myHandTypes.append(hand.classification[0].label)
        return myHands, myHandTypes


width, height = 1280, 720
cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)

findHands = mpHands(2)
paddleWidth, paddleHeight = 25, 125
paddleColor = (0, 255, 0)

xDelta, yDelta = 11, 8
speedIncrement = 2
speedCap = 24

LeftPlayer, RightPlayer = 0, 0
x_position, y_position = width // 2, height // 2
ballRad = 30
font = cv2.FONT_HERSHEY_SIMPLEX
myString = 'Game On'

try:
    while True:
        _, frame = cam.read()
        frame = cv2.flip(frame, 1)
        handData, myHandTypes = findHands.Marks(frame)
        
        for hand, handType in zip(handData, myHandTypes):
            if handType == 'Left':
                leftPaddle = hand[8][1]
                cv2.rectangle(frame, (0, int(leftPaddle - paddleHeight / 2)), (paddleWidth, int(leftPaddle + paddleHeight / 2)), paddleColor, -1)
            if handType == 'Right':
                rightPaddle = hand[8][1]
                cv2.rectangle(frame, (width - paddleWidth, int(rightPaddle - paddleHeight / 2)), (width, int(rightPaddle + paddleHeight / 2)), paddleColor, -1)
        
        # Ball Movement
        x_position += xDelta
        y_position += yDelta
        
        if y_position - ballRad <= 0 or y_position + ballRad >= height:
            yDelta *= -1
        if x_position - ballRad <= paddleWidth and leftPaddle - paddleHeight // 2 < y_position < leftPaddle + paddleHeight // 2:
            xDelta *= -1
        if x_position + ballRad >= width - paddleWidth and rightPaddle - paddleHeight // 2 < y_position < rightPaddle + paddleHeight // 2:
            xDelta *= -1
        
        # Scoring
        if x_position - ballRad <= 0:
            RightPlayer += 1
            x_position, y_position = width // 2, height // 2
            xDelta = min(xDelta + speedIncrement * (1 if xDelta > 0 else -1), speedCap)
            yDelta = min(yDelta + speedIncrement * (1 if yDelta > 0 else -1), speedCap)
            if RightPlayer == 3:
                myString = 'Right Wins!!'
                RightPlayer = 0
                xDelta, yDelta = 11, 8  # Reset speed after a win
        
        if x_position + ballRad >= width:
            LeftPlayer += 1
            x_position, y_position = width // 2, height // 2
            xDelta = min(xDelta + speedIncrement * (1 if xDelta > 0 else -1), speedCap)
            yDelta = min(yDelta + speedIncrement * (1 if yDelta > 0 else -1), speedCap)
            if LeftPlayer == 3:
                myString = 'Left Wins!!'
                LeftPlayer = 0
                xDelta, yDelta = 11, 8  # Reset speed after a win
        
        # Draw Ball and UI
        cv2.circle(frame, (x_position, y_position), ballRad, (255, 0, 255), -1)
        cv2.putText(frame, str(LeftPlayer), (5 * paddleWidth, 3 * paddleWidth), font, 1, (255, 0, 0), 2)
        cv2.putText(frame, str(RightPlayer), (width - 5 * paddleWidth, 3 * paddleWidth), font, 1, (255, 0, 0), 2)
        cv2.putText(frame, myString, (int(0.4 * width), 3 * paddleWidth), font, 1, (255, 0, 0), 2)
        
        cv2.imshow('Pong Game', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

except KeyboardInterrupt:
    cam.release()
    sys.exit()

cam.release()
cv2.destroyAllWindows()

# Now the ball speed is capped at 24, and it resets after each win. Let me know if you want any adjustments! 🚀
