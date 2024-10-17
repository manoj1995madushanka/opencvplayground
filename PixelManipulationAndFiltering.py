import numpy as np
import cv2

color = cv2.imread("butterfly.jpg")

gray = cv2.cvtColor(color,cv2.COLOR_BGR2GRAY)
cv2.imwrite("gray.jpg",gray)
cv2.imshow("gray.jpg",gray)

# belo one is easy more that cv2.split method
b = color[:,:,0]
g = color[:,:,1]
r = color[:,:,2]

rgba  = cv2.merge((b,g,r,g))
cv2.imwrite("rgba.png",rgba)
cv2.imshow("rgba.png",rgba)

cv2.waitKey(0)
cv2.destroyAllWindows()