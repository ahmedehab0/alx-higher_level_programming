#!/usr/bin/python3

"""defines a class"""


class Square:
    """class that represents a square"""
    def __init__(self, size=0):
        """initializing a class.
        Args:
            self (int): size of the square.
        Raises:
            TypeError: if size is not integer.
            ValueError: if size < 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an int")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """getter method"""
        return self.__size

    @size.setter
    def size(self, value):
        """setter method
            Args:
                value: value to be set
        """
        if not isinstance(value, int):
            raise TypeError("size must be an int")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """method that returns the current square area
        Args:
            no args.
        """
        return self.__size ** 2
