import cv2
import numpy as np
cap=cv2.VideoCapture(0)
import time
font = cv2.FONT_HERSHEY_PLAIN

while True:
    
    _,img=cap.read()
    img=cv2.resize(img,None,fx=1,fy=1)
    cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    #img=cv2.GaussianBlur(img,(5,5),0)
    img=cv2.bilateralFilter(img,11,75,75)
    canny=cv2.Canny(img,255,0)
    canny=cv2.dilate(canny,None,iterations=3)
    canny=cv2.erode(canny,None,iterations=1)
    contours,_=cv2.findContours(canny,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    contours=sorted(contours,key= lambda x:cv2.contourArea(x),reverse=True)
    i=0
    for cnt in contours:
        if 2000<cv2.contourArea(cnt)<7000:
            x,y,w,h=cv2.boundingRect(cnt)
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
            cv2.putText(img,"object"+str(i), (x, y), font, 2,
                    (255, 0, 0), 2)
            i+=1
    cv2.imshow('frame',img)  
    if cv2.waitKey(10)&0xff==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()    
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
