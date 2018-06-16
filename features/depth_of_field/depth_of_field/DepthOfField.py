import depth_of_field.blur  as bl
import depth_of_field.depth as de
import depth_of_field.blur_factor as blur_factor
import matplotlib.pyplot as plt
import sys
import os
#import blur_factor as blf
from sys import argv
from scipy import misc

#  get the picture path and use functions to work
#  the statements in the code is the function to complete
def DepthOfField(i_path):
	dimg = de.depth(i_path[1])
	fimg = blur_factor.blur_factor(dimg)
	'''
	dimg is image with depth axis
	fimg is image with blur factor axis
	'''
	# image_depth = de.depth(i_path[1],300)
	# img = misc.imread(i_path[1])
#   factor = blf.blur_factor()
	after = bl.blur(img,fimg)
#  	after = bl.blur(img,image_depth,factor)
	plt.imshow(after)
	plt.show()
	# show the picture after process

if __name__ == '__main__':
	start(sys.argv)
