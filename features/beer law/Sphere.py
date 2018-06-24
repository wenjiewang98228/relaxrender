from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

class Sphere(object):
    
    def __init__(self,r,color):
        self.r = r
        self.color = color
    
    def setLight(self):
        light_position = [1.0, 1.0, -1.0, 1.0]
        light_ambient  = [0.2, 0.2, 0.2, 1.0]
        light_diffuse  = [1.0, 1.0, 1.0, 1.0]
        light_specular = [1.0, 1.0, 1.0, 1.0]

        glLightfv(GL_LIGHT0, GL_POSITION, light_position)
        glLightfv(GL_LIGHT0, GL_AMBIENT,  light_ambient)
        glLightfv(GL_LIGHT0, GL_DIFFUSE,  light_diffuse)
        glLightfv(GL_LIGHT0, GL_SPECULAR, light_specular)

        glEnable(GL_LIGHT0)
        glEnable(GL_LIGHTING)
        glEnable(GL_DEPTH_TEST)

    def setMatirial(self,mat_diffuse,mat_shininess):
        mat_specular = [0.0, 0.0, 0.0, 1.0]
        mat_emission = [0.0, 0.0, 0.0, 1.0]

        glMaterialfv(GL_FRONT, GL_AMBIENT_AND_DIFFUSE, mat_diffuse)
        glMaterialfv(GL_FRONT, GL_SPECULAR,  mat_specular)
        glMaterialfv(GL_FRONT, GL_EMISSION,  mat_emission)
        glMaterialf (GL_FRONT, GL_SHININESS, mat_shininess)

    def make(self):
        #设置光源
        self.setLight()
        
        glDepthMask(GL_FALSE)
        
        self.setMatirial(self.color, 30.0)
        glPushMatrix()
        glTranslatef(0, 0, 13)
        glutSolidSphere(self.r, 30, 30)
        glPopMatrix()
        
        glDepthMask(GL_TRUE)

        
