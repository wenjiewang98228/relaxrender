'''
gamma 函数
变量一览
输入：
	img   --  输入数据 
	类型为 array,三维(高度,宽度,3)
	gamma --  参数值
	决定对比度修改程度（仅仅对gamma校正有用）
	funs  --  调用的校正函数
	默认为1为gamma校正，2为log校正，3为inverse log校正
	plot  --  是否绘图
	默认不绘图	
	save  --  是否输出中间结果
	默认为0不输出，其他值为输出
	saveFileName  --  选择保存图片名字
	如果不保存，可以不设置
'''
import numpy as np

def gamma_correction(img,gamma=2.2 ,funs=1 ,plot=0 ,save=0 ,saveFileName = 'gamma'):
	
    # 图片预处理 
    xmax = img.max()
    x = img/img.max()

    # 选择处理函数
    if funs == 1:
        img_new = x**gamma
    elif funs == 2:
        img_new = np.log(1+x)
    elif funs == 3:
        img_new = 2**x-1

    # 是否绘图
    if plot:
        import matplotlib.pyplot as plt
        plt.imshow(img_new)
        plt.show()

    # 是否输出
    if save:
        from skimage import io  
        io.imsave(str(saveFileName) + ".jpg",img_new)  

	
    return img_new
