import cv2
import numpy as np

cap = cv2.VideoCapture(0)
back = cv2.imread('./image.jpg')

while cap.isOpened():
    ret,frame = cap.read()
    
    if ret:
        #how do we convert rgb to hsv?
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
        l_red = np.array([0,100,100])
        u_red = np.array([10,255,255])
        
        mask = cv2.inRange(hsv, l_red, u_red)
        #cv2.imshow("mask",mask)
        
        part1 = cv2.bitwise_and(back, back ,mask=mask)
        #cv2.imshow("part1",part1)
        
        mask = cv2.bitwise_not(mask)
        
        part2 = cv2.bitwise_and(frame,frame,mask=mask)
        # cv2.imshow("mask",part2)
        cv2.imshow("cloak",part1+part2)
        
        if cv2.waitKey(5) == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()