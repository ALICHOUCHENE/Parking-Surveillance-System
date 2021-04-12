import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar
font = cv2.FONT_HERSHEY_PLAIN
cap=cv2.VideoCapture(0)
while True:
    _,frame = cap.read()
    decodedObjects = pyzbar.decode(frame)
    if len(decodedObjects)>0:
        for obj in decodedObjects:
            cv2.putText(frame, str(obj.data.decode('utf-8')), (50,50), font, 2,
                    (255, 0, 0), 3)
    cv2.imshow('frame',frame)     
    if cv2.waitKey(10) & 0xff == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()





