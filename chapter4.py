import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8)
# print(img)
# img[:] = 255,0,0

cv2.line(img,(0,0),(300,300),(0,255,0),3)  # green line
# cv2.rectangle(img,(0,0),(250,350),(255,30,10),2)
cv2.rectangle(img,(0,0),(250,350),(255,30,10),cv2.FILLED)

cv2.imshow("Image",img)
cv2.waitKey(0)