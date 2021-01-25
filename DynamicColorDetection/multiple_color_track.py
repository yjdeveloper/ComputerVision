# import libraries
import cv2 as cv 
import numpy as np 
import imutils

# Capturing the video feed
cap = cv.VideoCapture(0)

while True:
	# read the frames
	_, frame = cap.read()

	# convert to hsv
	hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

	# defining the Range of Red color
	red_lower = np.array([136,87,111],np.uint8)
	red_upper = np.array([180,255,255],np.uint8)

	# defining the Range of Blue color
	blue_lower=np.array([99,115,150],np.uint8)
	blue_upper=np.array([110,255,255],np.uint8)

	# defining the Range of yellow color
	yellow_lower=np.array([22,60,200],np.uint8)
	yellow_upper=np.array([60,255,255],np.uint8)

	# finding the range of red, blue, yellow color in the image
	red = cv.inRange(hsv, red_lower, red_upper)
	blue = cv.inRange(hsv, blue_lower, blue_upper)
	yellow = cv.inRange(hsv, yellow_lower, yellow_upper)

	# Morphological transformation, dilation
	kernel = np.ones((5, 5), "uint8")

	red = cv.dilate(red, kernel)
	res = cv.bitwise_and(frame, frame, mask = red)

	blue = cv.dilate(blue, kernel)
	res1 = cv.bitwise_and(frame, frame, mask = blue)

	yellow = cv.dilate(yellow, kernel)
	res2 = cv.bitwise_and(frame, frame, mask = yellow)    

	# tracking the red color
	cnts = cv.findContours(red, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
	cnts = imutils.grab_contours(cnts)

	for i, c in enumerate(cnts):
		area = cv.contourArea(c)
		if area > 300:
			(x, y, w, h) = cv.boundingRect(c)
			frame = cv.rectangle(frame, (x, y), (x + w, y + h), (0, 0,255), 2)
			cv.putText(frame, "RED color", (x, y), cv.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0,255))
	
	# tracking the blue color
	cnts = cv.findContours(blue, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
	cnts = imutils.grab_contours(cnts)

	for i, c in enumerate(cnts):
		area = cv.contourArea(c)
		if area > 300:
			(x, y, w, h) = cv.boundingRect(c)
			frame = cv.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
			cv.putText(frame, "BLUE color", (x, y), cv.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0))

	# tracking the yellow color
	cnts = cv.findContours(yellow, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
	cnts = imutils.grab_contours(cnts)

	for i, c in enumerate(cnts):
		area = cv.contourArea(c)
		if area > 300:
			(x, y, w, h) = cv.boundingRect(c)
			frame = cv.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 250), 2)
			cv.putText(frame, "YELLOW color", (x, y), cv.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 250))
	
	# show output
	cv.namedWindow("Color Tracking", cv.WINDOW_NORMAL)
	cv.imshow("Color Tracking", frame)

	# cv.namedWindow("Mask", cv.WINDOW_NORMAL)
	# cv.imshow("Mask", res)

	if cv.waitKey(10) & 0xFF == ord('q'):
		cap.release()
		cv.destroyAllWindows()
		break