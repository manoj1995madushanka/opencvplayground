import numpy as np
import cv2

# size height,width,channel, type
# uint8 means 2**8 = 256 maximum value
black = np.zeros([150,200,1],'uint8')
cv2.imshow("Black", black)
print(black[0,0,:])# prints all the pixel values of 0,0 location

ones = np.ones([150,200,3],'uint8')
cv2.imshow('Ones',ones)
print(ones[0,0,:])

white = np.ones([150,200,3],'uint16')
white *= (2**16-1)
cv2.imshow("White",white)
print(white[0,0,:])

color = ones.copy()
color[:,:] = (255,0,0)
cv2.imshow("Blue",color)
print(color[0,0,:])

cv2.waitKey(0)
cv2.destroyAllWindows()




