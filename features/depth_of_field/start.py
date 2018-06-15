import depth_of_field.blur as bl
import depth_of_field.depth as de
import matplotlib.pyplot as plt
import sys
import os
from sys import argv
from scipy import misc

#  the entry of the project
#  get the picture path from the cmd and use functions  
def start(i_path):
	if len(i_path)!= 2:
		print("Wrong number of parameters!")
	elif (os.path.exists(i_path[1]) and os.path.isfile(i_path[1])) == False:
		print("Wrong path of parameters!")
		# check whether the path of the picture is right
	else:
		image_depth = de.depth(i_path[1],300)		
		img = misc.imread(i_path[1])
		after = bl.blur(img,image_depth)
		plt.imshow(after)
		plt.show()
		# show the picture after process 

if __name__ == '__main__':
	start(sys.argv)


