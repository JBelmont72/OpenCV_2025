import mediapipe as mp
import sys
import cv2
print(cv2.__version__)
import numpy as np
print(f"This is version {sys.version}")
print(np.__version__)
import time
from handTrackModule import mpHands
# import handTrackModule as htm
# from htm import mpHands
# myObject = mpHands
# myObject=htm()
# frame,myHands,handsType=myObject.Marks(frame,draw=False)
# all_lmLists=myObject.findPostions(frame,draw=False)
# right_hand_coords, left_hand_coords   =myObject.labelHands(self, frame, myHands, handsType, draw=True)
def main():
    import cv2
    import time
    myObject = mpHands
    width = 1280
    height = 720
    cam = cv2.VideoCapture(1)
    cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
    cam.set(cv2.CAP_PROP_FPS, 30)
    cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

    findHands = mpHands(2)
    pTime = 0
    tips=[4,8,12,16,20]
    while True:
        ret, frame = cam.read()
        frame = cv2.resize(frame, (width, height))
        frame = cv2.flip(frame, 1)
        frame, handsLM, handsType = findHands.Marks(frame, draw=False)
        right_hand_coords, left_hand_coords = findHands.labelHands(frame, handsLM, handsType)
        if handsLM:  # Only proceed if any hands are detected
            lmList = findHands.findPositions(frame, draw=False)
            if lmList:
                print(lmList)
                # print(handsType) #output: ..., 26, 364], [20, 18, 319]]] ['Left']
                # print(handsLM)
        if right_hand_coords:
            # Perform action for right hand
            cv2.circle(frame, right_hand_coords, 20, (255, 0, 0), 2)  # Blue circle for right hand
        
        for hand,handType in zip(handsLM,handsType):## gives left and/or rignt and tuple
            # print(hand,handType)## a list of tuples of x and y
            if handType == 'Left':
                print(hand[8])
                cv2.circle(frame,hand[8],30,(255,0,0),3)
                for ind in tips:
                    cv2.circle(frame,hand[ind],25,(255,0,255),3)
        
        
        
        
        cv2.imshow('image',frame)
        if cv2.waitKey(1) & 0xff== ord('q'):
            cv2.destroyAllWindows()
            cam.release()
if __name__ == '__main__':
    main()