# import the necessary packages
from zernikemoments import ZernikeMoments
from imutils.paths import list_images
import numpy as np
import argparse
import pickle
import imutils
import cv2 as cv

# Construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path where the images will be stored")
# ap.add_argument("-i", "--index", required = True, help = "Path to where the index file will be stored")
args = vars(ap.parse_args())

# initialize our descriptor (Zernike Moments with a radius
# of 21 used to characterize the shape of our pokemon) and
# our index dictionary
desc = ZernikeMoments(8)

# loop over the sprite images
for spritePath in list_images(args["image"]):
	print(spritePath)
	# parse out the pokemon name, then load the image and
	# convert it to grayscale
	pokemon = spritePath[spritePath.rfind("/") + 1:].replace(".jpg", "")
	image = cv.imread(spritePath)
	image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
	# pad the image with extra white pixels to ensure the
	# edges of the pokemon are not up against the borders
	# of the image
	image = cv.copyMakeBorder(image, 15, 15, 15, 15,
		cv.BORDER_CONSTANT, value = 255)

	# initialize the outline image, find the outermost
	# contours (the outline) of the pokemone, then draw
	# it
	outline = np.zeros(image.shape, dtype = "uint8")
	cnts = cv.findContours(image.copy(), cv.RETR_EXTERNAL,
		cv.CHAIN_APPROX_SIMPLE)
	cnts = imutils.grab_contours(cnts)
	cnts = sorted(cnts, key = cv.contourArea, reverse = True)[0]
	cv.drawContours(outline, [cnts], -1, 255, -1)

	# compute Zernike moments to characterize the shape
	# of pokemon outline, then update the index
	moments = desc.describe(outline)

	print(moments.shape)