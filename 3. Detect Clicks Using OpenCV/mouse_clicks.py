# Import libraries
import cv2 as cv 
import numpy as np 

circles = np.zeros((4,2),np.int)
counter = 0

# define mouse points
def mousePoints(event,x,y,flags,params):
    global counter
    if event == cv.EVENT_LBUTTONDOWN:

        circles[counter] = x,y
        counter = counter + 1
        print(circles)

# load image
img = cv.imread("card.jpeg")
while True:
	width, height = 350, 250
	if counter == 4:
		pts1 = np.float32([circles[0], circles[1], circles[2], circles[3]])
		pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
		matrix = cv.getPerspectiveTransform(pts1, pts2)
		imgOutput = cv.warpPerspective(img, matrix, (width, height))
		cv.imshow("Output", imgOutput)
	
	# Display points
	for x in range(0, 4):
		cv.circle(img, (circles[x][0], circles[x][1]), 3, (0, 255, 0), cv.FILLED)

	cv.imshow("Original Image", img)
	# Call the function
	cv.setMouseCallback("Original Image", mousePoints)
	cv.waitKey(0)