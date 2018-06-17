from numpy import *

'''blur_factor

Deal with the depth axis from dimg, output image with blur_factor axis

args:
    dimg: numpy.ndarray type. Image with a depth axis.

return:
    fimg: numpy.ndarray type. Image with a blur_factor axis(total 4 axis).
    Blur_factor decide how much a pix will be blur.

'''
def blur_factor(dimg):
    fimg = dimg
    '''
    replace dimg's depth axis with blur factor axis
    '''
    return fimg
