import numpy as np
import cv2

img = cv2.imread('faces.jpeg', 1)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

h = hsv[:, :, 0]
s = hsv[:, :, 1]
v = hsv[:, :, 2]

hsv_split = np.concatenate((h, s, v), axis=1)
cv2.imwrite("HSV Split.jpg", hsv_split)

ret, min_sat = cv2.threshold(s, 40, 255, cv2.THRESH_BINARY)
cv2.imwrite("Sat Filter.jpg", min_sat)

ret1, max_hue = cv2.threshold(h, 15, 255, cv2.THRESH_BINARY_INV)
cv2.imwrite("Hue Filter.jpg", max_hue)

final = cv2.bitwise_and(min_sat, max_hue)
cv2.imwrite("Final.jpg", final)
cv2.imwrite("Original.jpg", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
