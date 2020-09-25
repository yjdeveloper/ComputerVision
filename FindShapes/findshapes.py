# import all the libraries
import argparse as ap
import cv2 as cv 
import numpy as np
import imutils

# constructor for argument parser
args = ap.ArgumentParser()
args.add_argument("-i", "--image", required=True, help="Path to the image")
arg = vars(args.parse_args())

# Load the image
original_image = cv.imread(arg["image"])
print("Shape: Original Image", original_image.shape)

# converting to grayscale
gray = cv.cvtColor(original_image, cv.COLOR_BGR2GRAY)
print("Shape: Grayscaled Image",gray.shape)
cv.imshow("Original Image", original_image)
cv.waitKey(0)

# Thresholding (Optional)
ret, thresh = cv.threshold(gray, 127, 255, 1)
cv.imshow("Threshold Image", thresh)
print(thresh.shape)
cv.waitKey(0)

contours = cv.findContours(thresh.copy(), cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
print ('Number of contours', str(len(contours)))
contours = imutils.grab_contours(contours)

for contour in contours:
	vertices = cv.approxPolyDP(contour, 0.01*cv.arcLength(contour,True), True)
	# Checking for Triangles
	if len(vertices) == 3:
		shape = 'Triangle'
		cv.drawContours(original_image, [contour], 0, (0,255,0), -1)
		M = cv.moments(contour)
		x = int(M['m10']/ M['m00'])
		y = int(M['m01']/ M['m00'])
		cv.putText(original_image, shape, (x-50, y), cv.FONT_ITALIC, 1,(0,0,0), 1)

	# Checking for square or rectangle	
	elif len(vertices) == 4:
		M = cv.moments(contour)
		x = int(M['m10']/ M['m00'])
		y = int(M['m01']/ M['m00'])
		x0, y0, width, height = cv.boundingRect(contour)

		if abs(width - height) <=3:
			shape = "Square"
			cv.drawContours(original_image, [contour], 0, (0,50,200), -1)
			cv.putText(original_image, shape, (x-50, y), cv.FONT_ITALIC, 1,(0,0,0), 1)
		else:
			shape = "Rectangle"
			cv.drawContours(original_image, [contour], 0, (0,150,255), -1)	
			M = cv.moments(contour)
			x = int(M['m10']/ M['m00'])
			y = int(M['m01']/ M['m00'])
			cv.putText(original_image, shape, (x-50, y), cv.FONT_ITALIC, 1, (0,0,0), 1)

	# Checking for pentagon		
	elif len(vertices) == 5:
		shape = "Pentagon"
		cv.drawContours(original_image, [contour], 0, (105,0,105), -1)	
		M = cv2.moments(contour)
		x = int(M['m10']/ M['m00'])
		y = int(M['m01']/ M['m00'])
		cv.putText(original_image, shape, (x-50, y), cv.FONT_ITALIC, 1, (0,0,0), 1)

	# Checking for Star shape
	elif len(vertices) == 10 or len(vertices) == 8:
		shape = "Star"
		cv.drawContours(original_image, [contour], 0, (0,0,105), -1)	
		M = cv.moments(contour)
		x = int(M['m10']/ M['m00'])
		y = int(M['m01']/ M['m00'])
		cv.putText(original_image, shape, (x-50, y), cv.FONT_ITALIC, 1, (0,0,0), 1)

	# Checking for Star	
	elif len(vertices) >=12:
		shape = "Circle"
		cv.drawContours(original_image, [contour], 0, (255,0,0), -1)	
		M = cv.moments(contour)
		x = int(M['m10']/ M['m00'])
		y = int(M['m01']/ M['m00'])
		cv.putText(original_image, shape, (x-50, y), cv.FONT_ITALIC, 1, (0,0,0), 1)
			
# Showing original image with shapes identified
cv.imshow("Identified Shapes", original_image)
cv.waitKey(0)
cv.destroyAllWindows()