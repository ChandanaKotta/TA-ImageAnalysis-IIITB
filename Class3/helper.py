import numpy as np
import scipy.ndimage.filters as filters
from skimage.filters import roberts
from skimage import feature
import cv2

def laplcian_of_gaussian(image):
	'''
	FINISH THIS FUNCTION:
	Two ways : 
	1) LoG(Image) = Lap[Gaussian(Image)]
	Gaussian filtering with some sigma, followed by laplace convolution.
	
	2) Derive LoG 
	Now check for zero crossings
	Define a custom threshold
	Zero-cross && threshold => Edge found!
	'''

	# REFERENCE: https://gist.github.com/Seanny123/10452462	


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

	g = np.sqrt(gx * gx + gy * gy)
	g *= 255.0 / np.max(g)
	return g


def roberts_filter(im):
	im = im.astype(np.float)
	width, height, c = im.shape
	if c > 1:
		img = cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
		# img = 0.2126 * im[:,:,0] + 0.7152 * im[:,:,1] + 0.0722 * im[:,:,2]
	else:
		img = im

	kh = np.array([[-1, 0], [0, 1]], dtype = np.float)
	kv = np.array([[0, 1], [-1, 0]], dtype = np.float)

	gx = signal.convolve2d(img, kh, mode='same', boundary = 'symm', fillvalue=0)
	gy = signal.convolve2d(img, kv, mode='same', boundary = 'symm', fillvalue=0)

	g = np.sqrt(gx * gx + gy * gy)
	g *= 255.0 / np.max(g)
	return g




def generateDetector(image, edgeDetector, custom = 0, only_x=1):
	if edgeDetector == 'prewitt':
			dx = filters.prewitt(image, 0)  # horizontal derivative
			dy = filters.prewitt(image, 1)  # vertical derivative
			mag = np.hypot(dx.astype('int32'), dy.astype('int32'))  # magnitude
			mag *= 255.0 / np.max(mag)  # normalize (Q&D)
			return mag
	
	elif edgeDetector == "sobel":
		if custom == 1:
			return sobel_filter(image)
		else :
			dx = filters.sobel(image, 0)  # horizontal derivative
			dy = filters.sobel(image, 1)  # vertical derivative
			mag = np.hypot(dx.astype('int32'), dy.astype('int32'))  # magnitude
			mag *= 255.0 / np.max(mag)  # normalize (Q&D)
			if only_x ==1:
				return dx 
			return mag

	elif edgeDetector == "log":
		if custom == 0:
			print("No in-built function available for log edge filter. Construct custom filter laplacian_of_gaussian and call generateDetector(image,'log',1)")
			return filters.gaussian_laplace(image, 0.01, output=None, mode='reflect', cval=0.0)
		else:
			return laplcian_of_gaussian(image)

	elif edgeDetector == "roberts":
		if custom == 0:
			return roberts(image)
		if custom == 1:
			return roberts_filter(image)
	elif edgeDetector == "canny":

		# image = image.astype(np.uint8)
		from scipy import ndimage, misc
		misc.imsave('fileName.jpg', image)
		image = ndimage.imread('fileName.jpg',0)

		return cv2.Canny(np.uint8(image),250,255,3)#,L2gradient=False)

		# return feature.canny(np.uint8(image), sigma = 100)
	else:
		# lower threshold- 25, upper threshold- 255
		return cv2.Canny(image,25,255)

