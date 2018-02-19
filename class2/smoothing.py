import cv2
import numpy as np
from matplotlib import pyplot as plt


img = cv2.imread('ROSYVn.jpg')
averagingBlur=cv2.blur(img,(5,5)) #or cv2.boxFilter(img,(5,5))
gaussblur = cv2.GaussianBlur(img,(5,5),0)
medianBlur= cv2.medianBlur(img,5)
bilateralBlur=cv2.bilateralFilter(img,15,80,80)
cv2.imshow('AveragingBlur.jpg',averagingBlur)
cv2.imshow('GaussianBlur.jpg',gaussblur)
cv2.imshow('MedianBlur.jpg',medianBlur)
cv2.imshow('Bilateralblur.jpg',bilateralBlur)
cv2.waitKey(0)
cv2.destroyAllWindows()
