import unittest
from depth_of_field import DepthOfField
class TestDepthOfField(unittest.TestCase):
    
    def testDepthOfField(self):
        DepthOfField.DepthOfField(["./", "./depth_of_field/city.png"])
