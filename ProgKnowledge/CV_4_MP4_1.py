'''this is a blog that looks good and is current
https://www.codingforentrepreneurs.com/blog/how-to-record-video-in-opencv-python/
https://joelmasters.medium.com/how-to-record-video-from-a-camera-using-opencv-and-python-on-mac-3f4306aa710b

Adapted from: https://stackoverflow.com/questions/29317262/opencv-video-saving-in-python/45868817
If your videos are being saved as ~6kb files, there is likely a size mismatch between the resolution of the camera and the VideoWriter.
DID not WORK!

'''


import cv2
cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (w,h))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret:
        out.write(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
out.release()
cv2.destroyAllWindows()
