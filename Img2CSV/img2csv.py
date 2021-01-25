import os, array
import pandas as pd
import time
import glob
from PIL import Image

columnNames = list()
for i in range(7500):
	pixel = 'pixel'
	pixel += str(i)
	columnNames.append(pixel)

train_data = pd.DataFrame(columns=columnNames)
start_time = time.time()
filenames = [img for img in glob.glob("/Users/admin/Desktop/ComputerVisions/Img2CSV/resize/*.jpg")]
ul = len(filenames)+1

for i in range(1, ul):
	t = i
	img_name = str(t)+'.jpg'
	img = Image.open("/Users/admin/Desktop/ComputerVisions/Img2CSV/resize/"+img_name)
	rawData = img.load()
	data = []
	for y in range(100):
		for x in range(75):
			data.append(rawData[x, y][0])

	print(i)
	k=0
	train_data.loc[i] = [data[k] for k in range(7500)]

print("Done")
print(time.time()-start_time)

train_data.to_csv("testcopy.csv",index = False)
print("Done1")
print(time.time()-start_time)