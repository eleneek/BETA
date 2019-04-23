import cv2
import numpy as np
cap = cv2.VideoCapture(0)
while True:
  _, frame = cap.read()
  hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
  lower_green = np.array([66,122,129])
  upper_green = np.array([86,255,255])
  lower_yellow = np.array([23,59,119])
  upper_yellow = np.array([54, 255,255])
  lower_red = np.array([150,150,50])
  upper_red = np.array([180,255,150])
  mask3 = cv2.inRange(hsv,lower_green,upper_green)
  mask1 = cv2.inRange(hsv,lower_yellow,upper_yellow)
  mask2 = cv2.inRange(hsv,lower_red,upper_red)
  mask = cv2.bitwise_or(mask1, mask2,mask3)
  res = cv2.bitwise_and(frame,frame,mask = mask)
  cv2.imshow("frame",frame)
  cv2.imshow("mask", mask)
  cv2.imshow("res",res)
  k = cv2.waitKey(5) &  0xFF
  if k == 27:
    break
cv2.destroyAllWindows()
cap.release()
