#!/usr/bin/python3
"""Inheris from baseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """a class to define rectangle using BaseGeometry"""

    def __init__(self, width, height):
        """Intialize a new Rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """method that returns the area"""
        return self.__width * self.__height

    def __str__(self):
        """str method that return the rectangle description"""
        descreption = "[" + str(self.__class__.__name__) + "] "
        descreption += str(self.__width) + "/" + str(self.__height)
        return descreption
