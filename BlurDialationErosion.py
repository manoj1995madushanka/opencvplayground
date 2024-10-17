import numpy as np
import cv2

image = cv2.imread("thresh.jpg")
cv2.imshow("Original",image)

blur = cv2.GaussianBlur(image,(5,55),0)
cv2.imshow("Blue",blur)


#  Dilation Erosion filter.
#  These are two operations that look to expand or contract the foreground
#  pixels of an image to help remove or accentuate small pixel details, such as speckles.
#  They work by sliding a kernel template, a small square, across an image, as displayed in the DilateVsErode image.
#  As you can see, the Dilation effect works to turn black pixels or background pixels into white pixels,
#  while an Erosion filter looks to turn white pixels into black pixels, essentially eating away at the foreground.

kernel = np.ones((5, 5), 'uint8')
dilate = cv2.dilate(image, kernel, iterations=1)
erode = cv2.erode(image, kernel, iterations=1)

cv2.imshow("Dilate",dilate)
cv2.imshow("Erode",erode)

cv2.waitKey(0)
cv2.destroyAllWindows()