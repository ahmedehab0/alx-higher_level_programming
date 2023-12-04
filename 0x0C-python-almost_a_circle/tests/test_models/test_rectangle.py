"""rectangle class testing module"""

import unittest
from models.rectangle import Rectangle
from models.base import Base

class TestRectangleClass(unittest.TestCase):
    def setUp(self):
        """setup method"""
        self.r1 = Rectangle(10, 5)

    def test_basic_cases(self):
        """basic cases testing"""
        self.r1.width = 5
        self.assertEqual(self.r1.width, 5)
        self.assertEqual(self.r1.id, 2)
    
    def test_assert_raises(self):
        """test if the methods raise errors correctly"""
        with self.assertRaises(TypeError):
            self.r1.width = 'p'
            self.y = '2'

        with self.assertRaises(ValueError):
            self.r1.wdith = -1
            self.r1.width = 0
            self.r1.x = -11
