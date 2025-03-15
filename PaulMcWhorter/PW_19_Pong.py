

# https://youtu.be/Y7Tww4fu5m8
# Gesture based game
# in zip
# l1=['left','right','left','right']
# # l1 = [[1, 2], [3, 4], [5, 6],[7,8]]
# l2=  [[7, 8], [9, 10], [11, 12],[13,14]]

 # Zipping list
# res = [(a, b) for a, b in zip(l1, l2)]
# print(res)
# for handType,hand in zip(l2,l1):
#     # print(hand,handType)
#     # print(type(hand),'   ',type(handType))
#     if hand =='left':
#         print('left handtype: ',hand,handType)
        
#          # Zipping list
# res = [(a, b) for a, b in zip(l1, l2) if 'left' in a]
# print(res)
### 2d optimaization to try to get faster action
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

xDelta, yDelta = 12, 15
speedIncrement = 1

LeftPlayer, RightPlayer = 0, 0
x_position, y_position = width // 2, height // 2
ballRad = 30
font = cv2.FONT_HERSHEY_SIMPLEX
myString = 'Game On'
lGameCount=0
rGameCount =0

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
            xDelta += speedIncrement * (1 if xDelta > 0 else -1)
            yDelta += speedIncrement * (1 if yDelta > 0 else -1)
            if RightPlayer == 3:
                myString = 'Right Wins!!'
                rGameCount+=1
                RightPlayer = 0
        
        if x_position + ballRad >= width:
            LeftPlayer += 1
            x_position, y_position = width // 2, height // 2
            xDelta += speedIncrement * (1 if xDelta > 0 else -1)
            yDelta += speedIncrement * (1 if yDelta > 0 else -1)
            if LeftPlayer == 3:
                myString = 'Left Wins!!'
                lGameCount +=1
                LeftPlayer = 0
        
        # Draw Ball and UI
        cv2.circle(frame, (x_position, y_position), ballRad, (255, 0, 255), -1)
        cv2.putText(frame, str(LeftPlayer), (4 * paddleWidth, 3 * paddleWidth), font, 1, (255, 0, 0), 2)
        cv2.putText(frame, str(RightPlayer), (width - 4 * paddleWidth, 3 * paddleWidth), font, 1, (255, 0, 0), 2)
        cv2.putText(frame, myString, (int(0.4 * width), 3 * paddleWidth), font, 1, (255, 0, 0), 2)
        cv2.putText(frame,str(lGameCount),(6*paddleWidth,3*paddleWidth)  ,font,1,(255,0,255),2)
        cv2.imshow('Pong Game', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

except KeyboardInterrupt:
    cam.release()
    sys.exit()

cam.release()
cv2.destroyAllWindows()

# This way, after every score, the ball speeds up progressively!





###~~~~~~optimized working two hand pong 1st optimaiztion  but running very slowly
# import cv2
# import sys
# import mediapipe as mp


# class mpHands:
#     def __init__(self, maxHands=2, tol1=0.5, tol2=0.5):
#         self.hands = mp.solutions.hands.Hands(
#             static_image_mode=False,
#             max_num_hands=maxHands,
#             min_detection_confidence=tol1,
#             min_tracking_confidence=tol2
#         )

#     def Marks(self, frame, width, height):
#         myHands = []
#         myHandTypes = []
#         frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#         results = self.hands.process(frameRGB)

#         if results.multi_hand_landmarks:
#             for handLandMarks in results.multi_hand_landmarks:
#                 myHand = [(int(landMark.x * width), int(landMark.y * height)) for landMark in handLandMarks.landmark]
#                 myHands.append(myHand)
            
#             for hand in results.multi_handedness:
#                 myHandTypes.append(hand.classification[0].label)
        
#         return myHands, myHandTypes


# width, height = 1280, 720
# cam = cv2.VideoCapture(0)
# cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
# cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
# cam.set(cv2.CAP_PROP_FPS, 30)
# cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

# findHands = mpHands(2)

# # Game variables
# paddleWidth, paddleHeight = 25, 125
# paddleColor = (0, 255, 0)
# ballRad = 30
# font = cv2.FONT_HERSHEY_SIMPLEX

# # Ball position and speed
# x_position, y_position = width // 2, height // 2
# xDelta, yDelta = 15, 12

# # Scores
# LeftPlayer, RightPlayer = 0, 0

# myString = 'Game On'

# try:
#     while True:
#         ret, frame = cam.read()
#         if not ret:
#             break
        
#         frame = cv2.flip(frame, 1)
#         frame = cv2.resize(frame, (width, height))

#         # Draw ball and scores
#         cv2.circle(frame, (x_position, y_position), ballRad, (255, 0, 255), -1)
#         cv2.putText(frame, str(LeftPlayer), (5 * paddleWidth, 3 * paddleWidth), font, 1, (255, 0, 0), 2)
#         cv2.putText(frame, str(RightPlayer), (width - 5 * paddleWidth, 3 * paddleWidth), font, 1, (255, 0, 0), 2)
#         cv2.putText(frame, myString, (int(0.4 * width), 3 * paddleWidth), font, 1, (255, 0, 0), 2)
        
#         handData, myHandTypes = findHands.Marks(frame, width, height)
        
#         leftPaddle, rightPaddle = height // 2, height // 2
        
#         for hand, handType in zip(handData, myHandTypes):
#             if handType == 'Left':
#                 leftPaddle = hand[8][1]
#                 cv2.rectangle(frame, (0, leftPaddle - paddleHeight // 2), (paddleWidth, leftPaddle + paddleHeight // 2), paddleColor, -1)
#             if handType == 'Right':
#                 rightPaddle = hand[8][1]
#                 cv2.rectangle(frame, (width - paddleWidth, rightPaddle - paddleHeight // 2), (width, rightPaddle + paddleHeight // 2), paddleColor, -1)

#         # Ball movement
#         x_position += xDelta
#         y_position += yDelta

#         # Ball collision with walls
#         if y_position - ballRad <= 0 or y_position + ballRad >= height:
#             yDelta *= -1

#         # Ball collision with paddles
#         if (x_position - ballRad <= paddleWidth and leftPaddle - paddleHeight // 2 <= y_position <= leftPaddle + paddleHeight // 2):
#             xDelta *= -1
#         elif (x_position + ballRad >= width - paddleWidth and rightPaddle - paddleHeight // 2 <= y_position <= rightPaddle + paddleHeight // 2):
#             xDelta *= -1
        
#         # Scoring
#         if x_position - ballRad <= 0:
#             RightPlayer += 1
#             x_position, y_position = width // 2, height // 2
#             if RightPlayer == 3:
#                 xDelta +=16
#                 yDelta +=6
#                 myString = 'Right Wins!!'
#                 RightPlayer = 0
        
#         if x_position + ballRad >= width:
#             LeftPlayer += 1
#             x_position, y_position = width // 2, height // 2
#             if LeftPlayer == 3:
#                 yDelta +=16
#                 xDelta +=6
#                 myString = 'Left Wins!!'
#                 LeftPlayer = 0
        
#         cv2.imshow('my WEBcam', frame)
#         cv2.moveWindow('my WEBcam', 0, 0)
        
#         if cv2.waitKey(1) & 0xff == ord('q'):
#             break
    
#     cam.release()
#     cv2.destroyAllWindows()
    
# except KeyboardInterrupt:
#     cam.release()
#     cv2.destroyAllWindows()
#     sys.exit()


####~~~~
# import cv2
# print(cv2.__version__)
 
# class mpHands:
#     import mediapipe as mp
#     def __init__(self,maxHands=2,tol1=.5,tol2=.5):
#         self.hands=self.mp.solutions.hands.Hands(static_image_mode=False, max_num_hands=2, min_detection_confidence=0.5, 
#      min_tracking_confidence=0.5)
#         # self.hands=self.mp.solutions.hands.Hands(False,maxHands,tol1,tol2)
#     def Marks(self,frame):
#         myHands=[]
#         frameRGB=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
#         results=self.hands.process(frameRGB)
#         if results.multi_hand_landmarks != None:
#             for handLandMarks in results.multi_hand_landmarks:
#                 myHand=[]
#                 for landMark in handLandMarks.landmark:
#                     myHand.append((int(landMark.x*width),int(landMark.y*height)))
#                 myHands.append(myHand)
#         return myHands
 
# width=1280
# height=720
# cam=cv2.VideoCapture(1)
# cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
# cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
# cam.set(cv2.CAP_PROP_FPS, 30)
# cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))
# findHands=mpHands(2)
# paddleWidth=125
# paddleHeight=25
# paddleColor=(0,255,0)
# while True:
#     ignore,  frame = cam.read()
#     frame=cv2.resize(frame,(width,height))
#     handData=findHands.Marks(frame)
#     for hand in handData:
#         cv2.rectangle(frame,(int(hand[8][0]-paddleWidth/2),0),(int(hand[8][0]+paddleWidth/2),paddleHeight),paddleColor,-1)
#     cv2.imshow('my WEBcam', frame)
#     cv2.moveWindow('my WEBcam',0,0)
#     if cv2.waitKey(1) & 0xff ==ord('q'):
#         break
# cam.release()
########~~~~~~~~~my version 22 Jan 2025
# import cv2
# print(cv2.__version__)
 
# class mpHands:
#     import mediapipe as mp
#     def __init__(self,maxHands=2,tol1=.5,tol2=.5):
#         self.hands=self.mp.solutions.hands.Hands(static_image_mode=False, max_num_hands=2, min_detection_confidence=0.5, 
#      min_tracking_confidence=0.5)
#         # self.hands=self.mp.solutions.hands.Hands(False,maxHands,tol1,tol2)
#     def Marks(self,frame):
#         myHands=[]
#         myHandTypes=[]
#         frameRGB=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
#         results=self.hands.process(frameRGB)
#         if results.multi_hand_landmarks != None:
#             for handLandMarks in results.multi_hand_landmarks:
#                 myHand=[]
#                 for landMark in handLandMarks.landmark:
#                     myHand.append((int(landMark.x*width),int(landMark.y*height)))
#                 myHands.append(myHand)
                
#             for hand in results.multi_handedness:
#                 myHandType=[]
#                 # print(hand)
#                 # print(hand.classification)
#                 # print( f"{hand.classification[0].index} is {hand.classification[0].label}")
#                 myHandType=hand.classification[0].label
#                 # myHandTypes.append(hand.classification[0].label)
#                 myHandTypes.append(myHandType)
                
        
        
        
        
#         return myHands,myHandTypes
 
# width=1280
# height=720
# cam=cv2.VideoCapture(1)
# cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
# cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
# cam.set(cv2.CAP_PROP_FPS, 30)
# cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))
# findHands=mpHands(2)
# paddleWidth=125
# paddleHeight=25
# paddleColor=(0,255,0)
# while True:
#     ignore,  frame = cam.read()
#     frame=cv2.resize(frame,(width,height))
#     handData,myHandTypes=findHands.Marks(frame)
#     for hand in handData:
#         # print(hand)
#         cv2.rectangle(frame,(int(hand[8][0]-paddleWidth/2),0),(int(hand[8][0]+paddleWidth/2),paddleHeight),paddleColor,-1)

#     for hand,handType in zip(handData,myHandTypes):
#         if handType=='Left':
#             handColor=(255,0,0)
#         if handType=='Right':
#             handColor=(0,0,255)
#         for ind in [0,5,6,7,8]:
#             cv2.circle(frame,hand[ind],15,handColor,5)
#             if  handType=='Left':
#                 cv2.putText(frame,'Left Hand',(hand[8][0],hand[8][1]),cv2.FONT_HERSHEY_SIMPLEX,2,(125,125,0),2)        
    
#     cv2.imshow('my WEBcam', frame)
#     cv2.moveWindow('my WEBcam',0,0)
#     if cv2.waitKey(1) & 0xff ==ord('q'):
#         break
# cam.release()
###~~~~13 March2025 took above and will move paddles ot side and add ball
# import cv2
# print(cv2.__version__)
 
# class mpHands:
#     import mediapipe as mp
#     def __init__(self,maxHands=2,tol1=.5,tol2=.5):
#         self.hands=self.mp.solutions.hands.Hands(static_image_mode=False, max_num_hands=2, min_detection_confidence=0.5, 
#      min_tracking_confidence=0.5)
#         # self.hands=self.mp.solutions.hands.Hands(False,maxHands,tol1,tol2)
#     def Marks(self,frame):
#         myHands=[]
#         myHandTypes=[]
#         frameRGB=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
#         results=self.hands.process(frameRGB)
#         if results.multi_hand_landmarks != None:
#             for handLandMarks in results.multi_hand_landmarks:
#                 myHand=[]
#                 for landMark in handLandMarks.landmark:
#                     myHand.append((int(landMark.x*width),int(landMark.y*height)))
#                 myHands.append(myHand)
                
#             for hand in results.multi_handedness:
#                 myHandType=[]
#                 # print(hand)
#                 # print(hand.classification)
#                 # print( f"{hand.classification[0].index} is {hand.classification[0].label}")
#                 myHandType=hand.classification[0].label
#                 # myHandTypes.append(hand.classification[0].label)
#                 myHandTypes.append(myHandType)
                
        
        
        
        
#         return myHands,myHandTypes
 
# width=1280
# height=720
# cam=cv2.VideoCapture(0)
# cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
# cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
# cam.set(cv2.CAP_PROP_FPS, 30)
# cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))
# findHands=mpHands(2)
# paddleWidth=125
# paddleHeight=25
# paddleColor=(0,255,0)
# while True:
#     ignore,  frame = cam.read()
#     frame=cv2.resize(frame,(width,height))
#     handData,myHandTypes=findHands.Marks(frame)
#     for hand in handData:
#         # print(hand)
#         cv2.rectangle(frame,(int(hand[8][0]-paddleWidth/2),0),(int(hand[8][0]+paddleWidth/2),paddleHeight),paddleColor,-1)

#     for hand,handType in zip(handData,myHandTypes):
#         if handType=='Left':
#             handColor=(255,0,0)
#         if handType=='Right':
#             handColor=(0,0,255)
#         for ind in [0,5,6,7,8]:
#             cv2.circle(frame,hand[ind],15,handColor,5)
#             if  handType=='Left':
#                 cv2.putText(frame,'Left Hand',(hand[8][0],hand[8][1]),cv2.FONT_HERSHEY_SIMPLEX,2,(125,125,0),2)        
    
#     cv2.imshow('my WEBcam', frame)
#     cv2.moveWindow('my WEBcam',0,0)
#     if cv2.waitKey(1) & 0xff ==ord('q'):
#         break
# cam.release()

## below is fautlty the right paddle hits were counting as misses and resetting to center width and height each time but only for the right paddle
# import cv2
# import sys
# print(cv2.__version__)
 
# class mpHands:
#     import mediapipe as mp
#     def __init__(self,maxHands=2,tol1=.5,tol2=.5):
#         self.hands=self.mp.solutions.hands.Hands(static_image_mode=False, max_num_hands=2, min_detection_confidence=0.5, 
#      min_tracking_confidence=0.5)
#         # self.hands=self.mp.solutions.hands.Hands(False,maxHands,tol1,tol2)
#     def Marks(self,frame):
#         myHands=[]
#         myHandTypes=[]
#         frameRGB=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
#         results=self.hands.process(frameRGB)
#         if results.multi_hand_landmarks != None:
#             for handLandMarks in results.multi_hand_landmarks:
#                 myHand=[]
#                 for landMark in handLandMarks.landmark:
#                     myHand.append((int(landMark.x*width),int(landMark.y*height)))
#                 myHands.append(myHand)
                
#             for hand in results.multi_handedness:
#                 myHandType=[]
#                 # print(hand)
#                 # print(hand.classification)
#                 # print( f"{hand.classification[0].index} is {hand.classification[0].label}")
#                 myHandType=hand.classification[0].label
#                 # myHandTypes.append(hand.classification[0].label)
#                 myHandTypes.append(myHandType)
#         return myHands,myHandTypes
 
# width=1280
# height=720
# cam=cv2.VideoCapture(0)
# cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
# cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
# cam.set(cv2.CAP_PROP_FPS, 30)
# cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))
# findHands=mpHands(2)
# paddleWidth=25
# paddleHeight=125
# paddleColor=(0,255,0)
# xDelta=11
# yDelta =8
# LeftPlayer =0
# RightPlayer = 0
# x_position=int(width/2)
# y_position = int(height/2)
# font = cv2.FONT_HERSHEY_SIMPLEX
# ballRad=30
# topEdge=y_position - int(ballRad/2)
# bottomEdge=y_position + int(ballRad/2)
# leftEdge = x_position - int(ballRad/2)
# rightEdge = x_position + int(ballRad/2)
# RightPlayer = 0
# LeftPlayer = 0
# myString = 'Game On'
# try:
#     while True:
#         ignore,  frame = cam.read()
#         frame=cv2.flip(frame,1)
#         frame=cv2.resize(frame,(width,height))
#         cv2.circle(frame,(x_position,y_position),ballRad,(255,0,255),-1)
#         cv2.putText(frame,str(LeftPlayer),(5*paddleWidth,3*paddleWidth),font,1,(255,0,0),2)
#         cv2.putText(frame,str(RightPlayer),(int(width-5*paddleWidth),3*paddleWidth),font,1,(255,0,0),2)
#         cv2.putText(frame,str(myString),(int(0.4 *width),3*paddleWidth),font,1,(255,0,0),2)
#         handData,myHandTypes=findHands.Marks(frame)
#         # for hand in handData:
#             # print(hand)
#             # cv2.rectangle(frame,(int(hand[8][0]-paddleWidth/2),0),(int(hand[8][0]+paddleWidth/2),paddleHeight),paddleColor,-1)

#         for hand,handType in zip(handData,myHandTypes):
#             if handType=='Left':
#                 handColor=(255,0,0)
#                 cv2.rectangle(frame,(0,int(hand[8][1]-paddleHeight/2)),(paddleWidth,int(hand[8][1]+paddleHeight/2)),paddleColor,-1)
#                 print(f'Left paddle y position: {hand[8][1]}')
#                 leftPaddle=hand[8][1]
#                 print(leftPaddle)
#             if handType=='Right':
#                 handColor=(0,0,255)
#                 cv2.rectangle(frame,(width-paddleWidth,int(hand[8][1]-paddleHeight/2)),(width,int(hand[8][1]+paddleHeight/2)),paddleColor,-1)
#                 rightPaddle=hand[8][1]
#             for ind in [0,5,6,7,8]:
#                 cv2.circle(frame,hand[ind],15,handColor,5)
#                 if  handType=='Left':
#                     cv2.putText(frame,'Left Hand',(hand[8][0],hand[8][1]),cv2.FONT_HERSHEY_SIMPLEX,2,(125,125,0),2)        
            
#             topEdge=y_position - int(ballRad/2)
#             bottomEdge=y_position + int(ballRad/2)
#             leftEdge = x_position - int(ballRad/2)
#             rightEdge = x_position + int(ballRad/2)
#             if topEdge  <=1*paddleWidth or bottomEdge>=(height-10):
#                 yDelta = (-1) * yDelta
#             if leftEdge<=paddleWidth and (y_position > int(leftPaddle -paddleHeight/2) and y_position < int(leftPaddle + paddleHeight/2)):
#                 xDelta =(-1) * xDelta
#             if rightEdge >= width-paddleWidth and y_position > int(rightPaddle -paddleHeight/2) and y_position < int(rightPaddle + paddleHeight/2):
#                 xDelta =(-1) * xDelta  
# ### next is if the ball misses the paddles at either end, lteft player misses, the right player gets one more point
#             if leftEdge<=paddleWidth and (y_position <= int(leftPaddle -paddleHeight/2) or y_position <=int(leftPaddle + paddleHeight/2)):
#                 x_position=int(width/2)
#                 y_position = int(height/2)
#                 RightPlayer =RightPlayer + 1 
#                 if RightPlayer ==5:
#                     RightPlayer=0    
#                     print('The right player wins')
#                     myString = 'Right Wins!!'
#             ## the right player misses. the left player scores one more point   
#             if rightEdge >= width-paddleWidth and (y_position < int(rightPaddle -paddleHeight/2) or y_position > int(rightPaddle + paddleHeight/2)):
#                 x_position=int(width/2)
#                 y_position = int(height/2)
#                 LeftPlayer = LeftPlayer +1
#                 if LeftPlayer ==5:
#                     LeftPlayer = 0 
#                     print('The left player wins') 
#                     myString='Left Wins!!'   
                            
#             y_position += yDelta
#             x_position += xDelta
#             print('y_position :',y_position)
  
#         cv2.imshow('my WEBcam', frame)
#         cv2.moveWindow('my WEBcam',0,0)
#         if cv2.waitKey(1) & 0xff ==ord('q'):
#             break
#     cam.release()  
    
# except KeyboardInterrupt:
#     cam.release()
#     sys.exit()
    
## 14 march this will be made into the two player pong fgame   
# import sys    
# import cv2
# print(cv2.__version__)
 
# class mpPose:
#     import mediapipe as mp
#     def __init__(self,still=False,upperBody=False, smoothData=True, tol1=.5, tol2=.5):
#         self.myPose=self.mp.solutions.pose.Pose(still,upperBody,smoothData,tol1,tol2)
#     def Marks(self,frame):
#         frameRGB=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
#         results=self.myPose.process(frameRGB)
#         poseLandmarks=[]
#         if results.pose_landmarks:
#             for lm in results.pose_landmarks.landmark:            poseLandmarks.append((int(lm.x*width),int(lm.y*height)))
#         return poseLandmarks
 
# class mpHands:
#     import mediapipe as mp
#     def __init__(self,maxHands=2,tol1=.5,tol2=.5):
#         self.hands=self.mp.solutions.hands.Hands(False,maxHands,tol1,tol2)
#     def Marks(self,frame):
#         myHands=[]
#         frameRGB=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
#         results=self.hands.process(frameRGB)
#         if results.multi_hand_landmarks != None:
#             for handLandMarks in results.multi_hand_landmarks:
#                 myHand=[]
#                 for landMark in handLandMarks.landmark:
#                     myHand.append((int(landMark.x*width),int(landMark.y*height)))
#                 myHands.append(myHand)
#         return myHands
 
# width=1280
# height=720
# cam=cv2.VideoCapture(4,cv2.CAP_DSHOW)
# cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
# cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
# cam.set(cv2.CAP_PROP_FPS, 30)
# cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))
 
# findHands=mpHands(2)
# findPose=mpPose()
# while True:
#     ignore,  frame = cam.read()
#     frame=cv2.resize(frame,(width,height))
#     handData=findHands.Marks(frame)
#     for hand in handData:
#         for ind in [0,5,6,7,8]:
#             cv2.circle(frame,hand[ind],25,(255,0,255),3)
#     poseData=findPose.Marks(frame)
#     if len(poseData)!=0:
#         cv2.circle(frame,poseData[0],5,(0,255,0),3)
 
#     cv2.imshow('my WEBcam', frame)
#     cv2.moveWindow('my WEBcam',0,0)
#     if cv2.waitKey(1) & 0xff ==ord('q'):
#         break
# cam.release()
# sys.exit()