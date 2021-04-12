import cv2
import numpy as np
cap=cv2.VideoCapture(0)
_,frame1=cap.read()
_,frame2=cap.read()

while True:
    d=cap.read()
    diff=cv2.absdiff(frame1,frame2)
    #frame1=cv2.resize(frame1,None,fx=0.5,fy=0.5)
    #frame2=cv2.resize(frame2,None,fx=0.5,fy=0.5)
    gray=cv2.cvtColor(diff,cv2.COLOR_BGR2GRAY)
    blur=cv2.GaussianBlur(gray,(5,5),0)
    #cv2.imshow("frame1",frame1)
    #cv2.imshow("frame2",frame2)
    #cv2.imshow("blur",blur)
    _,img=cv2.threshold(blur,30,255,cv2.THRESH_BINARY)
    img=cv2.dilate(img,None,iterations=3)
    #cv2.imshow("thresh",img)
    contours,_=cv2.findContours(img,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours :
        if 1500<cv2.contourArea(cnt) <4000:
            x,y,w,h=cv2.boundingRect(cnt)
            cv2.rectangle(frame1,(x,y),(x+w,y+h),(0,255,0),3)
    
    cv2.imshow("frame1",frame1)

    frame1=frame2
    _,frame2=cap.read()
    
    if cv2.waitKey(10) & 0xff==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()





