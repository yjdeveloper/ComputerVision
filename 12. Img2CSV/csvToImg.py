import csv
from PIL import Image
import numpy as np
import string
import os

csv_File_Path = "/Users/admin/Desktop/ComputerVisions/Img2CSV/mnist_test.csv"

count = 1
last_digit_Name =  None

image_Folder_Path = "/Users/admin/Desktop/ComputerVisions/Img2CSV/img"

Alphabet_Mapping_List = list(string.ascii_uppercase)

for alphabet in Alphabet_Mapping_List:
    path = image_Folder_Path + '/' + alphabet
    if not os.path.exists(path):
        os.makedirs(path)

with open(csv_File_Path, newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    count = 0
    for row in reader:
        digit_Name = row.pop(0)
        image_array = np.asarray(row)
        image_array = image_array.reshape(28, 28)
        new_image = Image.fromarray(image_array.astype('uint8'))

        if last_digit_Name != str(Alphabet_Mapping_List[(int)(digit_Name)]):
            last_digit_Name = str(Alphabet_Mapping_List[(int)(digit_Name)])
            count = 0
            print ("")
            print ("Prcessing Alphabet - " + str (last_digit_Name))
        
        image_Path = image_Folder_Path + '/' + last_digit_Name + '/' + str(count) + '.png'
        new_image.save(image_Path)
        count = count + 1