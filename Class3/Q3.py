'''
Author:Chandana Kotta 
(Original Code)

'''

from glob import glob
import numpy as np
import radialProfile
import cv2
import matplotlib.pyplot as plt


def fft(image, pw_spec = 0):
	F1 = np.fft.fft2(image)
	F2 = np.fft.fftshift( F1 )
		
	if pw_spec == 1:
	# Now shift the quadrants around so that low spatial frequencies are in
	# the center of the 2D fourier transformed image.
	
		return F2
	
	phase = np.angle(F2)
	magnitude = np.abs(F2)
	return magnitude, phase
	

def powerSpectrum(image): 
	# Take the fourier transform of the image.
	 
	# Calculate a 2D power spectrum
	psd2D = np.abs( fft(image,1) )**2
	return psd2D

nat_sum = np.zeros((400,400))
syn_sum = np.zeros((400,400))

for i in glob("images/nat*.png"):
	image = cv2.imread(i,0)
	image = cv2.resize(image,(400,400))
	nat_sum += np.array(powerSpectrum(image),dtype = np.uint8) 

for i in glob("images/syn*.png"):
	image = cv2.imread(i,0)
	image = cv2.resize(image,(400,400))
	syn_sum += np.array(powerSpectrum(image),dtype = np.uint8)

nat_avg = nat_sum/5.0
syn_avg = syn_sum/5.0


# cv2.imshow("natural",np.array(nat_avg, dtype = np.uint8))
# cv2.waitKey(0)
# cv2.imshow("synthetic",np.array(syn_avg, dtype = np.uint8))
# cv2.waitKey(0)


image_nat1 = cv2.imread("images/nat1.png")
image_nat2 = cv2.imread("images/nat2.png")

image_nat1 = cv2.resize(image_nat1,(400,400))
image_nat2 = cv2.resize(image_nat2,(400,400))

magnitude1, phase1 = fft(image_nat1)
magnitude2, phase2 = fft(image_nat2)


# f_ishift = np.fft.ifftshift(magnitude1)
# img_back = np.fft.ifft2(f_ishift)
# img_back = np.abs(img_back)

im_m1_p2 = magnitude1*np.exp(1j*phase2)
im_m1_p2 = np.fft.ifftshift(im_m1_p2)

im_m2_p1 = magnitude2*np.exp(1j*phase1)
im_m2_p1 = np.fft.ifftshift(im_m2_p1)


cv2.imshow("rec_m1_p2", np.array(np.abs(np.fft.ifft2(im_m1_p2)), dtype = np.uint8))
cv2.imshow("rec_m2_p1", np.array(np.abs(np.fft.ifft2(im_m2_p1)), dtype = np.uint8))

cv2.imshow("image_nat2",image_nat2)
cv2.imshow("image_nat1",image_nat1)

cv2.waitKey(0)


