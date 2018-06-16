import depth_of_field.blur  as bl
import depth_of_field.depth as de
import matplotlib.pyplot as plt
import sys
import os
#import blur_factor as blf
from sys import argv
from scipy import misc

#  get the picture path and use functions to work 
#  the statements in the code is the function to complete  
def DepthOfField(i_path):
	image_depth = de.depth(i_path[1],300)		
	img = misc.imread(i_path[1])
#   factor = blf.blur_factor()
	after = bl.blur(img,image_depth)
#  	after = bl.blur(img,image_depth,factor)
	plt.imshow(after)
	plt.show()
	# show the picture after process 

if __name__ == '__main__':
	start(sys.argv)


