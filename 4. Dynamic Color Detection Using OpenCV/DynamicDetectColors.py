import cv2 as cv 
import numpy as np 

def nothing(x):
	pass

cap = cv.VideoCapture(0)

img = np.zeros((200, 512, 3), np.uint8)
img1 = np.zeros((200,512, 3), np.uint8)

cv.namedWindow("HSV Value", cv.WINDOW_NORMAL)

cv.createTrackbar("H MIN", "HSV Value", 0, 179, nothing)
cv.createTrackbar("S MIN", "HSV Value", 0, 255, nothing)
cv.createTrackbar("V MIN", "HSV Value", 0, 255, nothing)

cv.createTrackbar("H MAX", "HSV Value", 179, 179, nothing)
cv.createTrackbar("S MAX", "HSV Value", 255, 255, nothing)
cv.createTrackbar("V MAX", "HSV Value", 255, 255, nothing)

while True:
	_, frame = cap.read()
	hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

	h_min = cv.getTrackbarPos("H MIN", "HSV Value")
	s_min = cv.getTrackbarPos("S MIN", "HSV Value")
	v_min = cv.getTrackbarPos("V MIN", "HSV Value")
	h_max = cv.getTrackbarPos("H MAX", "HSV Value")
	s_max = cv.getTrackbarPos("S MAX", "HSV Value")
	v_max = cv.getTrackbarPos("V MAX", "HSV Value")

	lower_blue = np.array([h_min, s_min, v_min])
	upper_blue = np.array([h_max, s_max, v_max])

	hsv_min = "MIN H:{} S:{} V:{}".format(h_min, s_min, v_min)
	hsv_max = "MAX H:{} S:{} V:{}".format(h_max, s_max, v_max)

	img[:] = (h_min, s_min, v_min)
	img1[:] = (h_max, s_max, v_max)

	numpy_horizontal = np.hstack((img, img1))

	mask = cv.inRange(hsv, lower_blue, upper_blue)

	result = cv.bitwise_and(frame, frame, mask = mask)

	cv.putText(frame, hsv_min, (30, 50), cv.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3)
	cv.putText(frame, hsv_max, (30, 100), cv.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3)

	cv.namedWindow("Value", cv.WINDOW_NORMAL)
	cv.imshow("Value", frame)
	cv.namedWindow("Mask", cv.WINDOW_NORMAL)
	cv.imshow("Mask", mask)
	cv.namedWindow("Frame Mask", cv.WINDOW_NORMAL)
	cv.imshow("Frame Mask", result)
	cv.namedWindow("Colors", cv.WINDOW_NORMAL)
	cv.imshow("Colors", numpy_horizontal)
	
	key = cv.waitKey(100) & 0xFF
	if key == ord('q'):
		break
	elif key != 255:
		print('key:',[chr(key)])
		
cap.release()
cv.destroyAllWindows()
