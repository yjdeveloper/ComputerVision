# import necessary packages
import cv2 as cv 
import numpy as np 
from matplotlib import pyplot as plt 

# load the image
img = cv.imread("img.jpg")
mask = np.zeros(img.shape[:2], np.uint8)

bgdModel = np.zeros((1, 65), np.float64)
fgdModel = np.zeros((1, 65), np.float64)

rect = (340, 265, 480, 392)

cv.grabCut(img, mask, rect, bgdModel, fgdModel, 5, cv.GC_INIT_WITH_RECT)
mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')

img = img*mask2[:, :, np.newaxis]
plt.imshow(img)
plt.colorbar()
plt.show()
