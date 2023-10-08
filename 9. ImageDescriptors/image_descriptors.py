# Harris
import cv2 as cv
import numpy as np 

# img = cv.imread("roated.jpg")
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# gray = np.float32(gray)

# harris = cv.cornerHarris(gray, 2, 3, 0.04)
# # take harris greater than 0.01 (1%)
# img[harris > 0.01*harris.max()] = [255, 0, 0]
# cv.imshow("Harris", img)
# cv.waitKey(0)

# Shi-Tomasi
img = cv.imread("monkey.jpg")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

corners = cv.goodFeaturesToTrack(gray, 25, 0.01, 10)
corners = np.int32(corners)
for i in corners:
	x, y = i.ravel()
	cv.circle(img, (x, y), 3, 255, -1)
cv.imshow("Shi-Tomasi", img)
cv.waitKey(0)

