# read and write images , grayscale

import cv2

colorful = cv2.imread('../images/colorful.jpg')
# colorful = cv2.imread('../images/colorful.jpg')

# grayscale reading
gray = cv2.imread('../images/colorful.jpg',0)

cv2.imshow("display",colorful)
cv2.imshow("display-gray",gray)


blue = colorful[:,:,0]
green = colorful[:,:,1]
red = colorful[:,:,2]

cv2.imshow("blue-channel",blue)
cv2.imshow("green-channel",green)
cv2.imshow("red-channel",red)

cv2.waitKey(0)
# cv2.destroyAllWindows()
