import numpy as np
import cv2

img = cv2.imread("faces.jpeg",1)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
path = "haarcascade_eye.xml"

eye_cascade = cv2.CascadeClassifier(path)

# change scale factor to minimize false positives and false negatives
eyes = eye_cascade.detectMultiScale(gray, scaleFactor=1.02, minNeighbors=20, minSize=(10,10))
print(len(eyes))

for (x, y, w, h) in eyes:
    # get the central values
	xc = (x+x+w)/2
	yc = (y+y+h)/2
	radius = w/2
	cv2.circle(img,(int(xc),int(yc)),int(radius),(255,0,0), 2)

cv2.imshow("Eyes",img)

cv2.waitKey(0)
cv2.destroyAllWindows()