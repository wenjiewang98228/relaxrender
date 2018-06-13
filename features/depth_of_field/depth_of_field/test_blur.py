import unittest

# test: run without corrupts.

import matplotlib.pyplot as plt  
from scipy import misc
from scipy import ndimage
import numpy
import depth_of_field.blur as bl

class TestBlur(unittest.TestCase):

    def test_blur(self) :
        
        # run for a coverage test only.
        colorImg = numpy.array([
            [[100,200,100], [200,100,200]],
            [[0,0,200], [0,0,0]]     
        ])
        
        depthImg = numpy.array([
            [[0], [5]],
            [[7], [11]]
        ])
        
        img = bl.blur(colorImg, depthImg)
        
        plt.imshow(img)
        plt.show()
        misc.imsave('img.png',img)
