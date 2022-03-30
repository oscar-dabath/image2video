import cv2
import numpy as np
import os
from os.path import isfile, join

import time
timestr = time.strftime("%d-%m-%Y_%H-%M-%S")
print (timestr)

val = input("Enter your custom file name: ")
print(val)

pathIn= '/img/'
pathOut = str(timestr)+str(val)+'_video.mp4'
fps = 24
frame_array = []
files = [f for f in os.listdir(pathIn) if isfile(join(pathIn, f))]

print('.\n.\n.\n.\n.\n.\n.\n..\n...\n....')
for i in range(2,len(files)):
    print('#',i,end='\r')
    filename=pathIn + str(i)+'_test.jpg'
    #reading each files
    img = cv2.imread(filename)
    height, width, layers = img.shape
    size = (width,height)
    #inserting the frames into an image array
    frame_array.append(img)
out = cv2.VideoWriter(pathOut,cv2.VideoWriter_fourcc(*'DIVX'), fps, size)
for i in range(len(frame_array)):
    # writing to a image array
    out.write(frame_array[i])
out.release()
