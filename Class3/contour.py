import numpy as np
import cv2
im = cv2.imread('threshold.png')
imgray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
'''The function cv::findContours describes the contour of areas consisting of ones. 
The areas in which you are interested are black/gray, though.
'''

# imgray = 255 - imgray
# ret, thresh = cv2.threshold(imgray, 250, 255, 0)
ret, thresh = cv2.threshold(imgray, 0, 100, 0)

im2, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(im, contours, -1, (0,255,0), 3)
cv2.imshow("as",im)
cv2.waitKey(0)
