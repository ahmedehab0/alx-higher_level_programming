#!/usr/bin/python3

"""square class module"""

from models.base import Base
from models.rectangle import Rectangle

class Square(Rectangle):
    """defines a square"""
    def __init__(self, size, x=0, y=0, id=None):
        """initialization method"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.heigth = value

    def __str__(self):
        """module string represation of square
        """
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(self.id,
                                                         self.x,
                                                         self.y,
                                                         self.width)
    def update(self, *args, **kwargs):
        """module update square
        """
        if len(args):
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.size = arg
                elif i == 2:
                    self.x = arg
                elif i == 3:
                    self.y = arg
        else:
            for key, value in kwargs.items():
                if hasattr(self, key) is True:
                    setattr(self, key, value)
    def to_dictionary(self):
       """method that returns the dictionary representation of a square"""
       dictionary = {"id" : self.id, "size" : self.size, "x" : self.x,
                     "y" : self.y}
       return dictionary
