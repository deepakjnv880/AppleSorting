import red_green
import size_sorting
import cv2
from PIL import Image
import numpy as np
# import CNN_test

filename="./try.jpg"

im = cv2.imread(filename)
im = cv2.resize(im, (500,500))
im=Image.fromarray((im).astype(np.uint8))
im.save("try.jpg")

is_red=False
is_big=False
# is_good=False
Angle=-1


# COLOR
color_of_apple = red_green.getcolor(filename)
if(color_of_apple == "RED"):
	is_red=True

# SIZE
size_of_apple = size_sorting.getsize(filename)
if(size_of_apple == "BIG"):
	is_big=True

# # QUALITY
# quality_of_apple = CNN_test.quality(filename)
# if(quality_of_apple=="GOOD"):
# 	is_good=True

# WRITE 8 combinations and angle accordingly

if(is_red and is_big==False):
	Angle = 0

if(is_red and is_big):
	Angle = 15

if(is_red==False and is_big==False):
	Angle = 30

if(is_red==False and is_big):
	Angle = 45

print(Angle)
