import numpy as np
import cv2

# this method used relative threshold value rather than global threshold value
img = cv2.imread('sudoku.png', 0)  # 0 means it is black and white
cv2.imshow("Original", img)

# basic thresholding
ret, thresh_basic = cv2.threshold(img, 70, 255, cv2.THRESH_BINARY)
cv2.imshow("Basic Binary Thresholding", thresh_basic)

# Adaptive thresholding
thresh_adapt = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 2)
cv2.imshow("Adaptive Thresholding", thresh_adapt)

cv2.waitKey(0)
cv2.destroyAllWindows()
