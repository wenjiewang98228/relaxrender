import unittest
from  Cube import Cube
from  Sphere import Sphere
from viewer import Viewer

class TestViewer(unittest.TestCase):

    def test_main(self):
        t=Viewer()
        t.main_loop()
        assert True
        

