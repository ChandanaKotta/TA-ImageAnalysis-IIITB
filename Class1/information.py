# play with bits
import cv2
import numpy as np

mona_lisa = cv2.imread("mona.jpg")
height, width, channels = mona_lisa.shape

bit_number = 0

cv2.imshow("mona",mona_lisa)
cv2.waitKey(0)

fused = np.zeros((height,width,3))
for i in range(height):
	for j in range(width):
		
		b,g,r = mona_lisa[i,j]

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

