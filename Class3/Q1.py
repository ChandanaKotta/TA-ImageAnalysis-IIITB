'''
Author:Chandana Kotta 
(Original Code - not retrieved from any online source)

'''

from skimage.util import random_noise as noise
import cv2
import numpy as np
from helper import generateDetector

def quantifyMeasure(image, edge_map):
	# take the canny edge map as the perfect edge map
	# and perform some math to quantify other edge maps ?
	# Do-it-yourself


chessboard = np.ones((800,800),dtype=np.uint8)*255
# chessboard[0:799,0:799] = 255
print(chessboard.shape)

for i in range(0,chessboard.shape[0],100):
	for j in range(0, chessboard.shape[1],200):
		if (i/100) %2 == 0:
			chessboard[i:i+100,j:j+100] = 0
		else: 
			chessboard[i:i+100,j+100:j+200] = 0

copy_one = chessboard
copy_two = chessboard


noisy_one=noise(chessboard, mode='gaussian', seed=None, clip=True,var =0.1)
noisy_two=noise(chessboard,mode='gaussian', seed=None, clip=True,var =0.01)



'''
EDGE FILTERS ON IMAGE

cv2.imshow("edge-sobel",generateDetector(chessboard, "sobel"))#, only_x =0 ))
cv2.imshow("prewitt",generateDetector(chessboard, "prewitt" ))
cv2.imshow("edge-roberts",generateDetector(chessboard, "roberts" ))

# Confusing result ? - COMPLETE THE FUNCTION
cv2.imshow("edge-log",generateDetector(chessboard, "log" ))

# CANNY
# chessboard = np.uint8(chessboard)
cv2.imshow("edge-canny",generateDetector(chessboard, "canny"))
cv2.imshow("chessboard",chessboard)
'''

# SOBEL
# cv2.imshow("edge-sobel-n1",generateDetector(noisy_one, "sobel"))#, only_x =0 ))
# cv2.imshow("edge-sobel-n2",generateDetector(noisy_two, "sobel"))#, only_x =0 ))

#PREWITT
# cv2.imshow("prewitt-n1",generateDetector(noisy_one, "prewitt" ))
# cv2.imshow("prewitt-n2",generateDetector(noisy_two, "prewitt" ))

# #ROBERTS
# cv2.imshow("edge-roberts-n1",generateDetector(noisy_one, "roberts" ))
# cv2.imshow("edge-roberts-n2",generateDetector(noisy_two, "roberts" ))

# CANNY
# cv2.imshow("edge-canny-n1",generateDetector(noisy_one, "canny"))

cv2.imshow("chessboard",chessboard)
cv2.imshow("chessboard-n1",noisy_one)
cv2.imshow("edge-canny",generateDetector(chessboard, "canny"))
cv2.imshow("edge-canny-n1",generateDetector(noisy_one, "canny"))
cv2.imshow("edge-canny-n2",generateDetector(noisy_two, "canny"))



cv2.waitKey(0)
# cv2.destroyAllWindows()


