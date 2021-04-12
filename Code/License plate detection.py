import cv2
import numpy as np
import pytesseract
pytesseract.pytesseract.tesseract_cmd=r"C:\Program Files\Tesseract-OCR\tesseract.exe"
img=cv2.imread("1.png")
img=cv2.resize(img,None,fx=1.5,fy=1.5)
h0,w0,c=img.shape

img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
print(pytesseract.image_to_string(img))
boxes=pytesseract.image_to_boxes(img)
for b in boxes.splitlines():
    b=b.split(' ')
    print(b)
    x,y,w,h=int(b[1]),int(b[2]),int(b[3]),int(b[4])
    cv2.rectangle(img,(x,h0-y),(w,h0-h),(0,255,0),2)
    cv2.putText(img,b[0],(x,h0-y),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
cv2.imshow("img",img)
cv2.waitKey(0)
