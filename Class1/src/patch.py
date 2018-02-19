import cv2
import numpy as np
colorful = cv2.imread('../images/colorful.jpg')
# colorful = cv2.imread("../images/colorful.jpg")

# dimensions using OpenCV
height, width, channels = colorful.shape

# dimensions using numpy
height = np.size(colorful, 0)
width = np.size(colorful, 1)
channels = np.size(colorful, 2)

print "height = ", height, "width = ", width,"channels = ",channels


#insert black patch

center_x = width/2
center_y= height/2
print center_x,center_y

colorful[center_y-50:center_y+50,center_x-50:center_x+50,1] = 0
cv2.imshow("patch_center",colorful)
cv2.waitKey(0)


