import cv2

Login = 'root'
Password = 'Deni$2001!'

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
