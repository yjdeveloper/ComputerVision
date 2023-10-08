# import libraries
import argparse
import imutils
import cv2 as cv 

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path to input image")
args = vars(ap.parse_args())

# load the image and perform pyramid mean shift filtering to aid the thresholding step
image = cv.imread(args["image"])
shifted = cv.pyrMeanShiftFiltering(image, 21, 51)
cv.imshow("Input", image)
cv.imshow("Mean Shift", shifted)
cv.waitKey()

# convert the mean shift image to grayscale, then apply Otsu's thresholding
gray = cv.cvtColor(shifted, cv.COLOR_BGR2GRAY)
thresh = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)[1]
cv.imshow("Thresh", thresh)

# find contours in the thresholded image
cnts = cv.findContours(thresh.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
print("[INFO] {} unique contours found".format(len(cnts)))

# loop over the contours
for (i, c) in enumerate(cnts):
	# draw contour
	((x, y), _) = cv.minEnclosingCircle(c)
	cv.putText(image, "#{}".format(i+1), (int(x) - 10, int(y)), cv.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)
	cv.drawContours(image, [c], -1, (0, 255, 0), 2)

# show the output
cv.imshow("Image",image)
cv.waitKey()

