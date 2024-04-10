import cv2
import numpy as np

cap = cv2.VideoCapture(0)

ret, frame1 = cap.read()
ret, frame2 = cap.read()

while cap.isOpened():
   
   dif=cv2.absdiff(frame1, frame2)
   gris=cv2.cvtColor(dif,cv2.COLOR_BGR2GRAY)

   lower_blue=np.array([38,36,0])
   upper_blue=np.array([121,255,255])
   mask=cv2.inRange(frame1,lower_blue,upper_blue)
   blur=cv2.GaussianBlur(gris, (5,5),0)
   
  # _,thresh = cv2.threshold (blur, 20,255,cv2.THRESH_BINARY)
   dilated=cv2.dilate(thresh,None, iterations=3)
   contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

   for contour in contours:
    (x,y,w,h) = cv2.boundingRect(contour)
    if cv2.contourArea(contour) < 1000:
        continue
    cv2.rectangle(frame1, (x,y),(x+w, y+h),(0,255,0),2)
    cv2.putText(frame1, "Estado: {}".format('Movement'), (10,20), cv2.FONT_HERSHEY_SIMPLEX, 
                1,(0,0,255), 3)
   #cv2.drawContours(frame1, contours, -1,(0,255,0), 2)

   cv2.imshow("Frame", frame1)
   cv2.imshow("Mask", mask)
   frame1=frame2
   ret,frame2=cap.read()
   key=cv2.waitKey(1)&0xff
   if key == ord('q'):
    break

cap.release()
cv2.destroyAllWindows()
