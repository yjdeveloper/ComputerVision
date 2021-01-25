import cv2 as cv 
from natsort import natsorted
import glob

width = 75
height = 100
dim = (width, height)

filenames = [img for img in glob.glob("/Users/admin/Desktop/ComputerVisions/Img2CSV/img/*.jpg")]
filenames =  natsorted(filenames)
i = 1
for file in filenames:
	img = cv.imread(file)
	img = cv.resize(img, dim, interpolation = cv.INTER_AREA)
	filename = str(i)+'.jpg'
	cv.imwrite(filename, img)
	i=i+1