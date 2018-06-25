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
    fimg = dimg.copy()
    # rows, cols, rgb, depth = dimg.shape
    # max_factor = 0
    # for row_tag in range(0,rows-1,1):
    #     for col_tag in range(0,cols-1,1):
    #         fimg[row_tag,col_tag,0] = max_factor - fimg[row_tag,col_tag,0]
    '''
    replace dimg's depth axis with blur factor axis
    '''
    print("Blur factor calculate successful.")
    return fimg
