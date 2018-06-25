from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from Sphere import *
from Cube import *
import numpy

red_color = [1.0, 0.0, 0.0, 1.0]
green_color = [0.0, 1.0, 0.0, 0.3333]
blue_color = [0.0, 0.0, 1.0, 0.5]


class Viewer(object):
    def __init__(self):
        self.init_interface()
        self.init_opengl()

    def init_interface(self):
        glutInit()
        glutInitWindowSize(640, 640)
        glutCreateWindow("3D Modeller")
        glutInitDisplayMode(GLUT_SINGLE | GLUT_RGBA)
        glutDisplayFunc(self.render)

    def init_opengl(self):
        """ 初始化opengl的配置 """
        #模型视图矩阵
        self.inverseModelView = numpy.identity(4)
        #模型视图矩阵的逆矩阵
        self.modelView = numpy.identity(4)

        
        glClearColor(0.4, 0.4, 0.4, 0.0)


    def render(self):
        #初始化投影矩阵
        self.init_view()

        #启动光照
        glEnable(GL_LIGHTING)
        #清除屏幕
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        #启动混合并设置混合因子
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        
        sphere = Sphere(0.3,red_color)
        sphere.make()
        cube = Cube(0.9,blue_color,0,0,13.7)
        cube.make()


        glutSwapBuffers()

    def init_view(self):
        xSize, ySize = glutGet(GLUT_WINDOW_WIDTH), glutGet(GLUT_WINDOW_HEIGHT)
        #得到屏幕宽高比
        aspect_ratio = float(xSize) / float(ySize)

        #设置投影矩阵
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        
        #设置视口，应与窗口重合
        glViewport(0, 0, xSize, ySize)
        #设置透视，摄像机上下视野幅度70度
        
        #视野范围到距离摄像机1000个单位为止。
        gluPerspective(70, aspect_ratio, 0.1, 1000.0)
        #摄像机镜头从原点后退15个单位
        glTranslated(0, 0, -15)
        
    def main_loop(self):
        #程序主循环开始


        glutSetOption(GLUT_ACTION_ON_WINDOW_CLOSE, GLUT_ACTION_GLUTMAINLOOP_RETURNS)


        glutMainLoop()
if __name__ == "__main__":
   viewer = Viewer()
   viewer.main_loop()
