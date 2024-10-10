import cv2
import os

Login = 'root'
Password = os.environ.get('CAMERA_PASSWORD')

cap = cv2.VideoCapture(f"rtsp://{Login}:{Password}@10.10.30.2:554/cam_1")

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret:
        cv2.imshow('frame', frame)
        if cv2.waitKey(20) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
