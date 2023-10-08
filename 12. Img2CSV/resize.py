import cv2 as cv
from natsort import natsorted
import glob
import shutil
import os

# Set the dimensions of the image
width = 75
height = 100
dim = (width, height)

# read files from the given folder
filenames = [img for img in glob.glob("/Users/admin/Desktop/ComputerVisions/Img2CSV/img/T/*.jpg")]
# sort the files in ascending order
filenames =  natsorted(filenames)

# shutil.rmtree('/Users/admin/Desktop/ComputerVisions/Img2CSV/resize/')

# Create directory
# if not os.path.exists("/Users/admin/Desktop/ComputerVisions/Img2CSV/resize"):
	# os.mkdir("/Users/admin/Desktop/ComputerVisions/Img2CSV/resize")

i = 659
for file in filenames:
	# read the file
	img = cv.imread(file)
	img = cv.resize(img, dim, interpolation = cv.INTER_AREA)
	filename = "/Users/admin/Desktop/ComputerVisions/Img2CSV/resize/"+str(i)+'.jpg'
	cv.imwrite(filename, img)
	i=i+1
