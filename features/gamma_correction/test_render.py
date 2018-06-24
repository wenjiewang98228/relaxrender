import unittest
from .render import *
from skimage import data


#测试类
class Test(unittest.TestCase):

#测试函数
    def test_gamma(self):    
        img = data.coffee()                  #测试图片
        gamma_correction(img,2.2,1,1,1)           #函数内调用我们的类 
        gamma_correction(img,2.2,2)
        gamma_correction(img,2.2,3)
     
        
        
