#https://docs.scipy.org/doc/scipy-0.8.x/reference/generated/scipy.ndimage.filters.gaussian_laplace.html

import scipy as sp
import numpy as np
import scipy.ndimage as nd
import matplotlib.pyplot as plt
import cv2 


face = sp.misc.face()
face = cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
LoG = nd.gaussian_laplace(face, 2)

cv2.imshow("face",face)
cv2.imshow("log",LoG)
cv2.waitKey(0)


