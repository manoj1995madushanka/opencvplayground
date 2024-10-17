import numpy as np
import cv2
from twisted.python.util import println

img = cv2.imread("output.jpg",1)
print(img) # printing image array

# image is a simply 2D numpy array
# print image array row size
print(type(img))
print(len(img))

# print image array columns in first row
print(img[0])

# access pixel value
print(img[0][1])

print("number of horizontal rows, columns and the number of channels ")
print(img.shape)