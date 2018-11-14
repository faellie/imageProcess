#This is following https://www.pyimagesearch.com/2016/02/01/opencv-center-of-contour/
# import the necessary packages
import argparse
import imutils
import cv2

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=False,
                help="path to the input image")
args = vars(ap.parse_args())

# load the image, convert it to grayscale, blur it slightly,
# and threshold it
#image = cv2.imread(args["image"])
image = cv2.imread('/opt/tmp/image/t2.jpg')
#image = cv2.resize(image, (1024, 800))
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#blurred = cv2.GaussianBlur(gray, (3, 3), 0)
thresh = cv2.threshold(gray, 60, 255, cv2.THRESH_BINARY)[1]
cv2.imshow("gray ", gray)
cv2.waitKey(0)

#cv2.imshow("blurred ", blurred)
#cv2.waitKey(0)

cv2.imshow("thresh ", thresh)
cv2.waitKey(0)

threshx = (255-thresh)

cv2.imshow("thresh reverted", threshx)
cv2.waitKey(0)

#th = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)
#cv2.imshow('Adaptive threshold',th)
#cv2.waitKey(0)

# find contours in the thresholded image
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
                        cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if imutils.is_cv2() else cnts[1]
# loop over the contours
for c in cnts:
    # compute the center of the contour
    M = cv2.moments(c)
    if(M["m00"] > 0.0):
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])

        # draw the contour and center of the shape on the image
        cv2.drawContours(image, [c], -1, (0, 255, 0), 2)
        cv2.circle(image, (cX, cY), 7, (255, 255, 255), -1)
        cv2.putText(image, "center", (cX - 20, cY - 20),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

# show the image
cv2.imshow("Image", image)
cv2.waitKey(0)

