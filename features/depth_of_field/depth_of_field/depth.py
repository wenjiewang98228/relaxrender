from scipy import misc
import numpy as np

'''depth

Receive an image and add a new depth axis to it. Axis is another expression of demension(in numpy).

args:
	img: numpy.ndarray type. The input image.

return:
	dimg: numpy.ndarray type. The input image with a new depth axis(totally 4 axis).

'''
def depth(img):
	if type(img)!=np.ndarray:
		print("TypeError: img is not a ndarray.")
	dimg = img
	dimg = dimg[:, :, :, np.newaxis]
	'''
	add depth dimension
	'''
	rows, cols, a = img.shape
	central = [rows/2,cols/2]
	for row_tag in range(0,rows-1,1):
		for col_tag in range(0,cols-1,1):
			dimg[row_tag,col_tag,0] = (pow(row_tag - entral[0],2)+pow(col_tag - central[1],2))/((pow(central[0],2)+pow(central[1],2)/pow(200,2))

	'''
	calculate depth according to the distance between pix and the centralself.
	maximum 200
	'''
	# for k in range(0, high, 1):
	# 	for j in range(cols):
	# 		dimg[k, j, 0] = 20
	# for k in range(high, rows, 1):
	# 	for j in range(cols):
	# 		dimg[k, j, 0] = 5

	return dimg
