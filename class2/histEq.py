#https://docs.scipy.org/doc/scipy-0.8.x/reference/generated/scipy.ndimage.filters.gaussian_laplace.html

import scipy as sp
import numpy as np
import scipy.ndimage as nd
import matplotlib.pyplot as plt
import cv2 


img = sp.misc.face()
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
equ = cv2.equalizeHist(img)
res = np.hstack((img,equ)) #stacking images side-by-side


clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
cl1 = clahe.apply(img)


cv2.imshow('original',img)
cv2.imshow('clahe_2.jpg',cl1)
cv2.imshow("eq",equ)
cv2.waitKey(0)


