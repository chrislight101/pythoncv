import cv2
import numpy as np

img = cv2.imread('circle.png',0)
ret,thresh = cv2.threshold(img,127,255,2)
contours,hierarchy = cv2.findContours(thresh,1,2)

cnt = contours[0]
M = cv2.moments(cnt)
cx = int(M['m10']/M['m00'])
cy = int(M['m01']/M['m00'])

cv2.line(img,(cx-20,cy),(cx+20,cy),50)
cv2.line(img,(cx,cy-20),(cx,cy+20),50)

epsilon = 0.1*cv2.arcLength(cnt,True)
approx = cv2.approxPolyDP(cnt,epsilon,True)

cv2.imshow("img",img)
cv2.waitKey(0)
