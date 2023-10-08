# Load libraries
import cv2 as cv 

vidcap = cv.VideoCapture("videos/17.mp4")

# function to extract frames
def getFrame(sec):
	vidcap.set(cv.CAP_PROP_POS_MSEC, sec * 1000)
	hasFrames, img = vidcap.read()
	if hasFrames:
		cv.imwrite("images/image"+str(count)+".jpg", img)
	return hasFrames

sec =  0
frameRate = 1 # it will capture the image in 0.5 seconds
count = 1
success = getFrame(sec)
while success:
	count += 1
	sec = sec + frameRate
	sec = round(sec, 2)
	success = getFrame(sec)
