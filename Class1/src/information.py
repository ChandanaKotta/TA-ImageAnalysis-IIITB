# play with bits
# the idea of this code is to illustrate the importance of bits in capturing information. 
# The bits to the left (in each pixel comprised of say 8 bits) capture the maximum amount of information. 

import cv2
import numpy as np

mona_lisa = cv2.imread("mona.jpg")
height, width, channels = mona_lisa.shape

# the position of the  bit that shall be manipulated.
bit_number = 0

cv2.imshow("mona",mona_lisa)
cv2.waitKey(0)

fused = np.zeros((height,width,3))
for i in range(height):
	for j in range(width):
		
		b,g,r = mona_lisa[i,j]
		
		# convert from uint8 to bits, replace each pixel's nth bit with 0. Repeat for all three channels. 
		b = np.unpackbits(b)
		b[bit_number] = 0

		g = np.unpackbits(g)
		g[bit_number] = 0

		r = np.unpackbits(r)
		r[bit_number] = 0

		mona_lisa[i,j,0] = np.packbits(b) 
		mona_lisa[i,j,1] = np.packbits(g)
		mona_lisa[i,j,2] = np.packbits(r)

cv2.imshow("altered",mona_lisa)
real_mona = cv2.imread("mona.jpg")

cv2.imshow("real",real_mona)

cv2.waitKey(0)

