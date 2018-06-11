import matplotlib.pyplot as plt  
from scipy import misc
from scipy import ndimage
from numpy import *

#img : the numpy array of picture
#dimg：the picture array with depth
#L1 : front depth of field   L2 : back depth of field
def blur(img,dimg,L1 = 1,L2 = 10):
	img1 = zeros(img.shape)
	for i in range(3):
		img1[:,:,i] = ndimage.gaussian_filter(img[:,:,i],sigma=5)
	blurimg = uint8(img1)
	
	rows,cols,a=img.shape
	for k in range(rows):
		for j in range(cols):
			if(dimg[k,j,0] < L1 or dimg[k,j,0] > L2)
				img[k,j]=blurimg[k,j]
	
	#plt.imshow(img)
	#plt.show()
	#misc.imsave('img.png',img)
	return img

