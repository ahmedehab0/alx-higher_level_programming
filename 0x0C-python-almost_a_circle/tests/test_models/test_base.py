#!/usr/bin/python3

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

"""testing module for the base class"""


class TestBaseClass(unittest.TestCase):
    def test_docstring(self):
        """checks for the docstrings"""
        self.assertIsNotNone(Base.__doc__)
        self.assertIs(hasattr(Base, "__init__"), True)
        self.assertIsNotNone(Base.__init__.__doc__)
        self.assertIs(hasattr(Base, "to_json_string"), True)
        self.assertIsNotNone(Base.to_json_string.__doc__)
        self.assertIs(hasattr(Base, "save_to_file"), True)
        self.assertIsNotNone(Base.save_to_file.__doc__)
        self.assertIs(hasattr(Base, "from_json_string"), True)
        self.assertIsNotNone(Base.from_json_string.__doc__)
        self.assertIs(hasattr(Base, "create"), True)
        self.assertIsNotNone(Base.create.__doc__)
        self.assertIs(hasattr(Base, "load_from_file"), True)
        self.assertIsNotNone(Base.load_from_file.__doc__)

    def test_id(self):
        """test id"""
        Base._Base__nb_objects = 0
        b1 = Base()
        b2 = Base()
        b3 = Base()

        b4 = Base(12)
        b5 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2) 
        self.assertEqual(b3.id, 3) 
        self.assertEqual(b4.id, 12) 
        self.assertEqual(b5.id, 4)

    def test_json_string(self):
        "test for the json_string methods"""
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        #self.assertEqual(dictionary, {'x': 2, 'width': 10, 'id': 5, 'height': 7, 'y': 8})
        #self.assertEqual(json_dictionary, [{'id': 5, 'width': 10, 'height': 7, 'x': 2, 'y': 8}])
        empty_list = Base.to_json_string([])
        self.assertEqual(empty_list, "[]")
        self.assertIs(type(dictionary), dict)
        self.assertIs(type(json_dictionary), str)
        
        #test from_json_string
        list_output = Base.from_json_string(json_dictionary)
        #self.assertEqual(list_output,dictionary)
        self.assertIs(type(list_output), list)

    def test_file_methods(self):
        """test save_to_file and load_from_file methods"""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(5, 2, 1, 4)
        R1 = [r1, r2]

        Rectangle.save_to_file(R1)
        R2 = Rectangle.load_from_file()
        self.assertNotEqual(R1, R2)




