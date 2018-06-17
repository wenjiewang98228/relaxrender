import depth_of_field.DepthOfField as dof
import sys
import os
from sys import argv

# the entry of the project 
def start(i_path):
	if len(i_path)!= 2:
		print("Wrong number of parameters!")
	elif (os.path.exists(i_path[1]) and os.path.isfile(i_path[1])) == False:
		print("Wrong path of parameters!")
		# check whether the path of the picture is right
	else:
		dof.DepthOfField(i_path)
# use the package to process the picture

if __name__ == '__main__':
	start(sys.argv)