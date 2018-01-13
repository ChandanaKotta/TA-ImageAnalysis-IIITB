# play with bits
# Extending the previous ideas about the most significant bits in pixels in the context of capturing information.
# This property can be exploited to fuse images. So may be used for encryption.
# In the following example, we will try to fuse Mr.Beans image over an image of Mona Lisa.

import cv2
import numpy as np

mona_lisa = cv2.imread("mona.jpg")
mr_bean = cv2.imread("mr_bean.jpg")

# Re-sizing mr.beans image to have the same dimensions as that of Mona Lisa.
mr_bean = mr_bean[:,100:700,:]
mr_bean = cv2.resize(mr_bean,(604,900))
print mona_lisa.shape
print mr_bean.shape

height, width, channels = mona_lisa.shape

number_of_bits = 2

cv2.imshow("mona",mona_lisa)
cv2.imshow("mr_bean",mr_bean)
cv2.waitKey(0)

fused = np.zeros((height,width,3))
for i in range(height):
	for j in range(width):
		
		b,g,r = mona_lisa[i,j]
		b2,g2,r2 = mr_bean[i,j]
		
		b = np.unpackbits(b)
		b2 = np.unpackbits(b2)
		fused_pixel_b = np.append(b[0:number_of_bits],b2[number_of_bits:8])

		g = np.unpackbits(g)
		g2 = np.unpackbits(g2)
		fused_pixel_g = np.append(g[0:number_of_bits],g2[number_of_bits:8])

		r = np.unpackbits(r)
		r2 = np.unpackbits(r2)
		fused_pixel_r = np.append(r[0:number_of_bits],r2[number_of_bits:8])


		mona_lisa[i,j,0] = np.packbits(fused_pixel_b) 
		mona_lisa[i,j,1] = np.packbits(fused_pixel_g)
		mona_lisa[i,j,2] = np.packbits(fused_pixel_r)

cv2.imshow("fused",mona_lisa)
real_mona = cv2.imread("mona.jpg")

cv2.imshow("real",real_mona)

cv2.waitKey(0)

