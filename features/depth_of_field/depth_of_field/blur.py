import matplotlib.pyplot as plt
from scipy import misc
from scipy import ndimage
from numpy import *

"""
blur the part of image that is out of DOF range
"""

# img : the numpy array of picture
# dimg：the picture array with depth
# L1 : front depth of field   L2 : back depth of field
# sigma : the degree of blurring of image

def blur(img,dimg,sigma=5,L1 = 1,L2 = 10):
	# img1 = zeros(img.shape)
	# for i in range(3):
	# 	img1[:,:,i] = ndimage.gaussian_filter(img[:,:,i],sigma)
	# blurimg = uint8(img1)
	#
	rows,cols,a=img.shape
	# for k in range(rows):
	# 	for j in range(cols):
	# 		if dimg[k,j,0] < L1 or dimg[k,j,0] > L2 :
	# 			img[k,j]=blurimg[k,j]

	blured = []
	for i in range(6):
		blured.append(zeros(img.shape))
	for i in range(6):
		for j in range(3):
			blured[i][:,:,j] = ndimage.gaussian_filter(img[:,:,j],i)
		print("Gaussian filter sigma",i)
	for k in range(rows):
		for j in range(cols):
			factor = int((dimg[k,j,0]/200)*6)
			if factor <= 5:
				img[k,j] = blured[factor][k,j]
			else:
				img[k,j] = blured[5][k,j]

	# for k in range(rows):
	# 	for j in range(cols):
	# 		sigma = int(dimg[k,j,0])
	# 		for i in range(3):
	# 			img1[k,j,i] = ndimage.gaussian_filter(img[k,j,i],sigma)#will use a lot of time


	# blurimg = uint8(img1)
	# for k in range(rows):
	# 	for j in range(cols):
	# 		img[k,j]=blurimg[k,j]
	print("Blur successful.")
	return img
