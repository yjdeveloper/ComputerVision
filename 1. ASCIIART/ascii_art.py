# load all the libraries
import cv2 as cv 

# read the image
img = cv.imread("football-ball.jpg")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# To convert an image into ascii, we need to map/draw a 
# letter or ascii symbol for each number in the image. 
# It is also not displayed the same as an image because we're 
# saving it to a text file or just printing it straight to the console.
# Below here I have a mapping set up for these numbers. 
# I chose a very simple scheme to use:
# Numbers 0-180 are represented by a 'W'
# Numbers 180+ are represented by a '!'
# This essentially creates a binary ascii image since there are 
# only two symbols at play in any transformation.
def setupAsciiMapping():
	characterSet = list(('W' * 18) + '!!!!!!!!')
	for i in range(26):
		for j in range(10):
			asciiToNum[i*10+j] = characterSet[i]
asciiToNum = {}
setupAsciiMapping()

transformedAscii = []

for i in gray:
	temp = []
	for j in i:
		temp.append(asciiToNum[j])
	transformedAscii.append(temp)
ascii = ''
for i in transformedAscii:
	ascii+= ' '.join(i)
	ascii+='\n'

print(ascii)
