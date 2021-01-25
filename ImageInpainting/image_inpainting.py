# import packages
import argparse
import cv2 as cv

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, required=True,
	help="path input image on which we'll perform inpainting")
ap.add_argument("-m", "--mask", type=str, required=True,
	help="path input mask which corresponds to damaged areas")
ap.add_argument("-a", "--method", type=str, default="telea",
	choices=["telea", "ns"], help="inpainting algorithm to use")
ap.add_argument("-r", "--radius", type=int, default=3,
	help="inpainting radius")
args = vars(ap.parse_args())

# initialize the inpainting algorithm to be the Telea et al. method
flags = cv.INPAINT_TELEA

# check to see if we should be using the avier-Stokes (i.e., Bertalmio et al.) method for inpainting
if args['method'] == "ns":
	flags = cv.INPAINT_NS

# Load the (1) input image (i.e., the image we're going to perform
# inpainting on) and (2) the  mask which should have the same input
# dimensions as the input image -- zero pixels correspond to areas
# that *will not* be inpainted while non-zero pixels correspond to
# "damaged" areas that inpainting will try to correct
image = cv.imread(args['image'])
mask = cv.imread(args["mask"])
mask = cv.cvtColor(mask, cv.COLOR_BGR2GRAY)

# perform inpainting using OpenCV
output = cv.inpaint(image, mask, args["radius"], flags=flags)

# show the original input image, mask and output after applying inpainting
cv.imshow("Original Image", image)
cv.imshow("Mask Image", mask)
cv.imshow("Output Image", output)
cv.waitKey(0)