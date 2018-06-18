from scipy import misc
import numpy as np

'''depth

Receive an image and add a new depth axis to it. Axis is another expression of demension(in numpy).

args:
	img: numpy.ndarray type. The input image.

return:
	dimg: numpy.ndarray type. The input image with a new depth axis(totally 4 axis).

'''

def cal_depth(row,col,central,maximum_dep):
	distance = (pow(row - central[0],2)+pow(col - central[1],2))
	maximum_distance = pow(central[0],2)+pow(central[1],2)
	return distance/maximum_distance*maximum_dep

def depth(img):
	if type(img)!=np.ndarray:
		print("TypeError: img is not a ndarray.")
	dimg = img.copy()
	dimg = dimg[:, :, :, np.newaxis]
	'''
	add depth dimension
	'''
	rows, cols, a = img.shape
	central = [rows/2,cols/2]
	for row_tag in range(rows):
		for col_tag in range(cols):
			dimg[row_tag,col_tag,0] = cal_depth(row_tag,col_tag,central,1)*200
			if dimg[row_tag,col_tag,0]>200:
				print("Calculate depth data error.")
			#ndarray can store 256 maximum in a axis

	'''
	calculate depth according to the distance between pix and the centralself.
	maximum 200
	'''
	print("Calculate depth data successful.")
	return dimg
