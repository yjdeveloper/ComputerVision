# import the necessary packages
from skimage.feature import peak_local_max
from skimage.morphology import watershed
from scipy import ndimage
import numpy as np
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

# convert the mean shift image to grayscale, then apply Otsu's thresholding
gray = cv.cvtColor(shifted, cv.COLOR_BGR2GRAY)
thresh = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)[1]
cv.imshow("Thresh", thresh)

# compute the exact Euclidean distance from every binary pixel to the nearest zero pixel, then find peaks in this distance map
D = ndimage.distance_transform_edt(thresh)
localMax = peak_local_max(D, indices=False, min_distance=20, labels=thresh)

# perform a connected component analysis on the local peaks, using 8-connectivity, then appy the Watershed algorithm
markers = ndimage.label(localMax, structure=np.ones((3, 3)))[0]
labels = watershed(-D, markers, mask=thresh)
print("[INFO] {} unique segments found".format(len(np.unique(labels)) - 1))

# loop over the unique labels returned by the Watershed algorithm
for label in np.unique(labels):
	# if the label is zero, we are examining the 'background' so simply ignore
	if label == 0:
		continue

	# otherwise, allocate memory for the label region and draw it on the mask
	mask = np.zeros(gray.shape, dtype="uint8")
	mask[labels == label] = 255

	# detect contours in the mask and grab the largest one
	cnts = cv.findContours(mask.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
	cnts = imutils.grab_contours(cnts)
	c = max(cnts, key=cv.contourArea)

	# draw a circle enclosing the object
	((x, y), r) = cv.minEnclosingCircle(c)
	cv.circle(image, (int(x), int(y)), int(r), (0, 255, 0), 2)
	cv.putText(image, "#{}".format(label), (int(x) - 10, int(y)), cv.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)


# show the output image
cv.imshow("Output", image)
cv.waitKey(0)
cv.waitKey()