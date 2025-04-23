import cv2
import numpy as np
## Facial Recognition System /Users/judsonbelmont/Documents/SharedFolders/OpenCV/OpenCV_2025/haar/haarcascade_frontalface_alt2.xml
##  /Users/judsonbelmont/Documents/SharedFolders/OpenCV/OpenCV_2025/haar/haarcascade_frontalface_default.xml
class FacialRecognitionSystem:
    def __init__(self, camera_index=1):
        self.camera_index = camera_index
        self.cap = cv2.VideoCapture(self.camera_index)
        self.face_cascade = cv2.CascadeClassifier('/Users/judsonbelmont/Documents/SharedFolders/OpenCV/OpenCV_2025/haar/haarcascade_frontalface_default.xml')
        self.smile_cascade = cv2.CascadeClassifier('/Users/judsonbelmont/Documents/SharedFolders/OpenCV/OpenCV_2025/haar/haarcascade_smile.xml')
        self.face_rect = None
        self.smile_rect = None
        self.is_smiling = False
        self.running = True

    def run(self):
       while self.running:
           ret, frame = self.cap.read()
           if not ret:
               print("Failed to grab frame")
               break

           gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
           faces = self.face_cascade.detectMultiScale(gray, 1.1, 4)
           smiles = self.smile_cascade.detectMultiScale(gray, 1.5, 4)
    
            # Draw rectangles around detected faces and smiles
           if len(faces) > 0:
               self.face_rect = faces[0]
           else:
               self.face_rect = None
               print("No face detected")
           for (x, y, w, h) in faces:
               self.face_rect = (x, y, w, h)
               print(f"Face detected at: {self.face_rect}")
               cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

               # Detect smile in the face region
               roi_gray = gray[y:y+h, x:x+w]
               print(roi_gray.shape)
               smiles = self.smile_cascade.detectMultiScale(roi_gray, 1.5, 4)
               if len(smiles) > 0:  
                   self.is_smiling = True
                #    cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
                   smile_roi = smiles[0]
                   sx, sy, sw, sh = smile_roi
                   print(f"Smile ROI: {smile_roi}")
                   cv2.circle(frame, (x + sx + int(sw/2), y + sy + int(sh/2)), 10, (0, 255, 125), -1)
                   cv2.rectangle(frame, (x + sx, y + sy), (x + sx + sw, y + sy + sh), (255, 255, 0), 2)
                   print("Smile detected")
                #    cv2.rectangle(frame, (x + int(w/2) - 10, y + int(h/2) - 10), (0, 255, 0), 2)
                   break  # Stop searching for faces after finding a smile
               else:
                   self.is_smiling = False

           cv2.imshow('Facial Recognition', frame)
           

           if cv2.waitKey(1) & 0xFF == ord('q'):
               self.running = False

       self.cap.release()
       cv2.destroyAllWindows()


if __name__ == '__main__':
   system = FacialRecognitionSystem()
   system.run()