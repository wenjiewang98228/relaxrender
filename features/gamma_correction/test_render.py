import unittest
from .render import *
from skimage import data


#以下是对测试类的定义
#test
#测试类
class Test(unittest.TestCase):

    
#下面编写测试函数
#定义测试函数
#包括导入测试图片
#包括调用函数的类
#测试函数
    def test_gamma(self):    
        img = data.coffee()                  #测试图片
        gamma_correction(img,2.2,1,1,1)           #函数内调用我们的类 
        gamma_correction(img,2.2,2)
        gamma_correction(img,2.2,3)
     
        
        
