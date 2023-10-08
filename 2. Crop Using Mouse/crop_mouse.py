import cv2 as cv 
from time import time

img = cv.imread("colorpic.jpg")

box = []
def draw_function(event, x, y, flags, params):
	t = time()
	# global x1, y1, x2, y2
	if event == cv.EVENT_LBUTTONDOWN:
		print("Starting mouse position: " +str(x)+ ", "+str(y))
		sbox = [x, y]
		box.append(sbox)
	elif event == cv.EVENT_LBUTTONUP:
		print("Ending mouse position:" +str(x)+ ", "+str(y))
		ebox = [x, y]
		box.append(ebox)
		print(box)
		# crop = img[startY:endY, startX:endX]
		print("startY", box[-2][1])
		print("endY", box[-1][1])
		print("startX", box[-2][0])
		print("endX", box[-1][0])
		crop = img[box[-2][1]:box[-1][1],box[-2][0]:box[-1][0]]
		cv.imshow("Crop", crop)
		cv.imwrite('Crop'+str(t)+'.jpg', crop)
		cv.waitKey(0)

cv.namedWindow("image")
cv.setMouseCallback('image', draw_function)


while (1):
	cv.imshow("image", img)
	k = cv.waitKey(20) & 0xFF
	if k == 27:
		cv.destroyAllWindows
		break