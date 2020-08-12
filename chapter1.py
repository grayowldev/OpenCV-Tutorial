import cv2
import numpy as np
# print("cv2 package imported")


img = cv2.imread("Resources/lena.png")

# cv2.imshow("Output",img)
# cv2.waitKey(0)


# cap = cv2.VideoCapture("Resources/test_video.mp4")
#webcam
# cap = cv2.VideoCapture(0)
# cap.set(3,640)
# cap.set(4,480)
#
# while True:
#     success, img = cap.read()
#     cv2.imshow("Video", img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

kernel = np.ones((5,5),np.uint8)

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(11,11),0)
# imgBlur2 = cv2.GaussianBlur(imgGray,(31,31),0)
imgCanny = cv2.Canny(img,100,100)
imgDialation = cv2.dialate(imgCanny,kernel,iterations=1)
imgEroded = cv2.erode(imgDialation,kernel,iteration=1)


cv2.imshow("Gray Image",imgGray)
cv2.imshow("Blur Image",imgBlur)
# cv2.imshow("More Blur Image",imgBlur2)
cv2.imshow("Canny Image",imgCanny)
cv2.imshow("Dialated image Image",imgDialation)
cv2.waitKey(0)