'''

'''
import cv2
import time
import datetime

cap = cv2.VideoCapture(1)
cap.set(4,480)
cap.set(3,640)

# cap.set(4,720)
# cap.set(3,1280)
# cap.set(4,720)
# cap.set(3,1080)
cap.set(cv2.CAP_PROP_FPS,30)
cap.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))


face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
body_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_fullbody.xml")

detection = False
detection_stopped_time = None
timer_started = False
SECONDS_TO_RECORD_AFTER_DETECTION = 5

frame_size = (int(cap.get(3)), int(cap.get(4)))
fourcc = cv2.VideoWriter_fourcc(*"mp4v")

while True:
    _, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    bodies = face_cascade.detectMultiScale(gray, 1.3, 5)

    if len(faces) + len(bodies) > 0:
        for face in faces:
            x,y,width,height=face
            cv2.rectangle(frame,(x,y),(int(x+width),int(y+height)),(255,0,0),3)
        if detection:
            timer_started = False
        else:                   ## detection starts out false, so hits here FIRST, flips detection to TRUE
            detection = True
            current_time = datetime.datetime.now().strftime("%d-%m-%Y-%H-%M-%S")
            out = cv2.VideoWriter(
                f"{current_time}.mp4", fourcc, 20, frame_size)
            print("Started Recording!")
    elif detection:     ## detection was turned TRUE, recording begins here
        if timer_started:       ##timer_started is false at this time and is flipped to TRUE in the else statement
            if time.time() - detection_stopped_time >= SECONDS_TO_RECORD_AFTER_DETECTION:
                detection = False
                timer_started = False
                out.release()
                print('Stop Recording!')
        else:
            timer_started = True
            detection_stopped_time = time.time()## this is ccontinually updated after the 'detection' became True until the if statement above is satisfied

    if detection:
        out.write(frame)

    # for (x, y, width, height) in faces:
    #    cv2.rectangle(frame, (x, y), (x + width, y + height), (255, 0, 0), 3)

    cv2.imshow("Camera", frame)

    if cv2.waitKey(1) == ord('q'):
        break

out.release()
cap.release()
cv2.destroyAllWindows()