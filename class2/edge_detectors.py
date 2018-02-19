import scipy as sp
import numpy as np
import scipy.ndimage as nd
import matplotlib.pyplot as plt
import cv2 
from scipy import signal
from scipy import ndimage
import numpy

def sobel_filter(im):

	im = im.astype(np.float)
	width, height, c = im.shape
	if c > 1:
		img = cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
		# img = 0.2126 * im[:,:,0] + 0.7152 * im[:,:,1] + 0.0722 * im[:,:,2]
	else:
		img = im


	kh = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]], dtype = np.float)
	kv = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]], dtype = np.float)

	gx = signal.convolve2d(img, kh, mode='same', boundary = 'symm', fillvalue=0)
	gy = signal.convolve2d(img, kv, mode='same', boundary = 'symm', fillvalue=0)


	cv2.imshow("sobel-edge-1",gx)
	cv2.imshow("sobel-edge-2",gy)
	cv2.waitKey(0)





	g = np.sqrt(gx * gx + gy * gy)
	g *= 255.0 / np.max(g)

	#plt.figure()
	#plt.imshow(g, cmap=plt.cm.gray)      

	return g

face = sp.misc.face()
# face = cv2.imread("beach.jpg")

#custom function
sobel = sobel_filter(face)


# using functions from scipy
face = cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
# face = face.astype('int32')

dx = ndimage.sobel(face, 0)  # horizontal derivative
dy = ndimage.sobel(face, 1)  # vertical derivative


mag = numpy.hypot(dx.astype('int32'), dy.astype('int32'))  # magnitude
mag *= 255.0 / numpy.max(mag)  # normalize (Q&D)


cv2.imshow("original",face)
cv2.imshow("sobel-edge-custom",sobel)
cv2.imshow("sobel-edge-y",dy)
cv2.imshow("sobel-edge-x",dx)

cv2.imshow("sobel-edge-inbuilt",mag)
cv2.waitKey(0)
