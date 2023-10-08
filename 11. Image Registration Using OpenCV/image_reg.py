'''
1. import 2 images
2. Convert to grayscale
3. Initiate ORB detector
4. Find Keypoints and describe them
5. Match keyspoints = Brute force matcher
6. RANSAC - Reject the bad keypoints
7. Register two images (Homography)
'''

import cv2 as cv
import numpy as np 

# Step 1
ref = cv.imread("monkey.jpg")
# image to be registered
reg = cv.imread("shear.jpg")

# Step 2
refGray = cv.cvtColor(ref, cv.COLOR_BGR2GRAY)
regGray = cv.cvtColor(reg, cv.COLOR_BGR2GRAY)

# Step 3
orb = cv.ORB_create(50)
# keypoints and descriptors
kpref, desref = orb.detectAndCompute(refGray, None)
kpreg, desreg = orb.detectAndCompute(regGray, None)

# Step 4
refPoints = cv.drawKeypoints(refGray, kpref, None, flags = None)
regPoints = cv.drawKeypoints(regGray, kpreg, None, flags = None)
cv.imshow("[KEYPOINTS] Normal", refPoints)
cv.imshow("[KEYPOINTS] Distorted", regPoints)
cv.waitKey(0)

# Step 5
matcher = cv.DescriptorMatcher_create(cv.DESCRIPTOR_MATCHER_BRUTEFORCE_HAMMING)
# Match the descriptors
matches = matcher.match(desreg, desref, None)
# Sort the descriptors based on the distancs
matches = sorted(matches, key = lambda x:x.distance)
drawMatches = cv.drawMatches(regGray, kpreg, refGray, kpref, matches[:10], None)
cv.imshow("[MATCHES]", drawMatches)
cv.waitKey(0)

# Step 6
points1 = np.zeros((len(matches), 2), dtype=np.float32)
points2 = np.zeros((len(matches), 2), dtype=np.float32)

# bunched of coordinates that we have identified
for i, match in enumerate(matches):
	# index of the descriptors
	points1[i, :] = kpreg[match.queryIdx].pt 
	points2[i, :] = kpref[match.trainIdx].pt 

# Step 7
h, mask = cv.findHomography(points1, points2, cv.RANSAC)
# use homography
height, width, channels = ref.shape
regRegister = cv.warpPerspective(reg, h, (width, height))
cv.imshow("[FINAL]", regRegister)
cv.waitKey(0)