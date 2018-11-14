import cv2
import imutils
import numpy as np


filename = '/opt/tmp/image/t1.jpg'
img = cv2.imread(filename)
img = imutils.resize(img, height=300)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Calcution of Sobelx
sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=3)

# Calculation of Sobely
sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=3)

mag, ang = cv2.cartToPolar(sobelx, sobely)

# Calculation of Laplacian
laplacian = cv2.Laplacian(img,cv2.CV_64F)

#cv2.imshow('sobelx',sobelx)
#cv2.imshow('sobely',sobely)
cv2.imshow('laplacian',laplacian)
laplacianBlured = cv2.GaussianBlur(laplacian, (11, 11), 0)
cv2.imshow('laplacianBlured',laplacianBlured)
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()
