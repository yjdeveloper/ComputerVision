import cv2 as cv 

# load image
img = cv.imread("nemo0.jpg")
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

b = hsv[:, :, 0]
g = hsv[:, :, 1]
r = hsv[:, :, 2]

cv.imshow("Original", img)
cv.imshow("Blue", b)
cv.imshow("Green", g)
cv.imshow("Red", r)
cv.waitKey()