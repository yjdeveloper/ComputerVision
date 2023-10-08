# import all the libraries
import numpy as np 
import cv2 as cv 
import imutils
import time

# Define variables
avg = None
video = cv.VideoCapture("people-capture.mp4")
xvalues = list()
motion = list()
count1 = 0
count2 = 0

# Define a function to count the people
def find_majority(k):
	myMap = {}
	maximum = ( '', 0) # occuring element
	for i in k:
		if i in myMap: 
			myMap[i] +=1
		else:
			myMap[i] = 1
		
		# keep track of maximum on the go
		if myMap[i] > maximum[1]:
			maximum = (i, myMap[i])
	return maximum

while True:
	frame = video.read()[1]
	flag = True
	text = ""

	frame = imutils.resize(frame, width = 500)
	gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
	gray = cv.GaussianBlur(gray, (21, 21), 0)

	if avg is None:
		print("[INFO] starting background model...")
		avg = gray.copy().astype('float')
		continue

	cv.accumulateWeighted(gray, avg, 0.5)
	frameDelta = cv.absdiff(gray, cv.convertScaleAbs(avg))
	thresh = cv.threshold(frameDelta, 5, 255, cv.THRESH_BINARY)[1]
	thresh = cv.dilate(thresh, None, iterations = 2)
	cnts = cv.findContours(thresh.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
	cnts = imutils.grab_contours(cnts)
	# iterate over the contours
	for c in cnts:
		if cv.contourArea(c) < 5000:
			continue
		(x, y, w, h) = cv.boundingRect(c)
		xvalues.append(x)
		cv.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
		flag = False
	
	no_x = len(xvalues)
	
	if no_x > 2:
		difference = xvalues[no_x - 1] - xvalues[no_x - 2]
		if difference > 0:
			motion.append(1)
		else:
			motion.append(0)
	
	if flag is True:
		if no_x > 5:
			val, times = find_majority(motion)
			if val == 1 and times >= 15:
				count1 += 1
			else:
				count2 += 1
		xvalues = list()
		motion = list()
	
	cv.line(frame, (260, 0), (260,480), (0,255,0), 2)
	cv.line(frame, (420, 0), (420,480), (0,255,0), 2)
	cv.putText(frame, "In : {}".format(count1), (10, 20), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
	cv.putText(frame, "Out : {}".format(count2), (10, 40), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
	cv.imshow("Frame", frame)
	cv.imshow("Gray", gray)
	cv.imshow("FrameDelta", frameDelta)

	key = cv.waitKey(1) & 0xFF
	if key == ord('q'):
		break 
video.release()
cv.destroyAllWindows()	
