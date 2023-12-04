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

    def area(self):
        """method that returns the current square area
        Args:
            no args.
        """
        return self.__size ** 2
