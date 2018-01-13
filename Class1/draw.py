# polygons and text
import numpy as np
import cv2

# Create a black image
img = np.zeros((600,600,3), np.uint8)
 
# Draw a diagonal yellow line with thickness of 5 px
# image, starting pixel, ending pixel, color in (R,G,B), thickness in pixels
# cv2.line(img,(0,0),(599,599),(0,255,255),5)
# cv2.line(img,(0,0),(599,599),(0,255,255),5)

# cv2.rectangle(img,(384,0),(510,128),(0,255,0),3)
# cv2.circle(img,(447,63), 63, (0,0,255), -1)
# cv2.ellipse(img,(256,256),(100,50),0,0,180,255,-1)

# #polygon

# pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
# pts = pts.reshape((-1,1,2))
# cv2.polylines(img,[pts],True,(0,255,0))

# font = cv2.FONT_HERSHEY_SIMPLEX
# cv2.putText(img,'Image Analysis Rocks!!',(10,500), font, 1.6,(255,255,255),2,cv2.LINE_AA)

cv2.imshow("image",img)
cv2.waitKey(0)