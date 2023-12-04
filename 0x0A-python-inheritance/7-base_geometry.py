#!/usr/bin/python3

"""module that defines a class"""


class BaseGeometry:
    """empty class"""

    def area(self):
        """area method
            Raises: Exception
        """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """function to validate value
        Args:
            name(str): a string.
            value(int: an int
        Raises:
            TypeError: if value is not an integer.
            ValueError: if value is less than 0.
        """

        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
