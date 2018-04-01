import numpy as np
import cv2
from skimage.segmentation import mark_boundaries
from skimage.segmentation import slic
from skimage.util import img_as_float
from skimage import io

img = cv2.imread('images/flowers.png')
image = img.reshape((-1,3))

# convert to np.float32
image = np.float32(image)

# define criteria, number of clusters(K) and apply kmeans()
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1)
K = 3
ret,label,center=cv2.kmeans(image,K,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)




# Now convert back into uint8, and make original image
center = np.uint8(center)
res = center[label.flatten()]
res2 = res.reshape((img.shape))

image_sk = img_as_float(io.imread("images/flowers.png"))

numSegments=15
segments = slic(image_sk, n_segments = numSegments, sigma = 2)



cv2.imshow('res2',res2)
cv2.waitKey(0)


# cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
cv2.imshow("slic",mark_boundaries(image_sk, segments))
cv2.waitKey(0)

cv2.destroyAllWindows()