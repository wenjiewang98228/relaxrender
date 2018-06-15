#import blur as bl
from scipy import misc
import numpy as np
#import matplotlib.pyplot as plt

#image path
#row from 0~300 got less depth
#row more than 300 got greater depth
#but the change is too obvious
def depth(path):
	img = misc.imread(path)
	dimg = misc.imread(path)
	dimg = dimg[:, :, :, np.newaxis]
	"""
	add depth dimension
	"""
	rows, cols, a = img.shape
	for k in range(0, 300, 1):
		for j in range(cols):
			dimg[k, j, 0] = 5
	for k in range(300, rows, 1):
		for j in range(cols):
			dimg[k, j, 0] = 20
#	img2 = bl.blur(img, dimg)
#	plt.imshow(img2)
#	plt.show()

	return dimg