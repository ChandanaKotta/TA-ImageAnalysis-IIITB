'''
CODE RETRIEVED FROM:

https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_imgproc/py_transforms/py_fourier_transform/py_fourier_transform.html
'''

import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('images/elon.jpg',0)

fft = np.fft.fft2(img)
fft_shift = np.fft.fftshift( fft )
	
# magnitude_spectrum = 20*np.log(cv2.magnitude(dft_shift[:,:,0],dft_shift[:,:,1]))

# plt.subplot(121),plt.imshow(img, cmap = 'gray')
# plt.title('Input Image'), plt.xticks([]), plt.yticks([])
# plt.subplot(122),plt.imshow(magnitude_spectrum, cmap = 'gray')
# plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
# plt.show()

rows, cols = img.shape
crow,ccol = int(rows/2) , int(cols/2)

# create a mask first, center square is 1, remaining all zeros
mask = np.zeros((rows,cols),np.uint8)
mask[crow-30:crow+30, ccol-30:ccol+30] = 1

mask2 = np.ones((rows,cols),np.uint8)
mask2[crow-30:crow+30, ccol-30:ccol+30] = 0

# apply mask and inverse DFT
# CHANGE MASK BELOW
fshift = fft_shift*mask2
f_ishift = np.fft.ifftshift(fshift)

img_back = np.fft.ifft2(f_ishift)
print(img_back.shape)


# plt.subplot(121),plt.imshow(img, cmap = 'gray')
# plt.title('Input Image'), plt.xticks([]), plt.yticks([])
# plt.subplot(122),plt.imshow(img_back, cmap = 'gray')
# plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
# plt.show()
print(img_back.shape)

cv2.imshow("image",img)
cv2.imshow("image_back",np.array(np.abs(img_back),dtype = np.uint8))
cv2.waitKey(0)


