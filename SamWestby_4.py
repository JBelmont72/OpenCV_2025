'''SamWestby -4.py 
https://www.youtube.com/watch?v=esmpHCJz8xI
Giovanni Code  His tutorial is using trackbars for edge detection!!

contour detection
https://www.youtube.com/watch?v=IBQYqwq_w14

'''
import cv2 # See video 1 for installation

# Replace "0" with a file path to work with a saved video
stream = cv2.VideoCapture(0)

if not stream.isOpened():
    print("No stream :(")
    exit()

fps = stream.get(cv2.CAP_PROP_FPS)
width = int(stream.get(3)) #1920 requires integers
height = int(stream.get(4))#1080
print("Frame width: ",width,
      '\n\t Frame height',height)
# list of FourCC video codes: https://softron.zendesk.com/hc/en-us/articles/207695697-List-of-FourCC-codes-for-video-codecs
output = cv2.VideoWriter("images/4_stream.mp4",
            cv2.VideoWriter_fourcc('m', 'p', '4', 'v'),
            fps=fps, frameSize=(width, height))
# look for fourcc code MPEG is MPG$ or MP4V
while True:
    ret, frame = stream.read()
    if not ret: # if no frames are returned
        print("No more stream :(")
        break
    # he sometimes has to resize the frame using 
    # frame= cv2.resize(frame,(width,height)) 
    # next line optional if want to resize.
    frame = cv2.resize(frame, (int(width/2), int(height/2)))
    
    
    output.write(frame)
    cv2.imshow("Webcam!", frame)
    if cv2.waitKey(1) == ord('q'): # press "q" to quit
        break

stream.release()
cv2.destroyAllWindows()