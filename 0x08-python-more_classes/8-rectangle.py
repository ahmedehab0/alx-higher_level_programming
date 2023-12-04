#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """Represent a rectangle."""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.
        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Get/set the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/set the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def perimeter(self):
        """method that returns the perimeter of a rectangle"""
        if self.__height == 0 or self.__width == 0:
            perimeter = 0
        else:
            perimeter = (self.__height + self.__width) * 2
        return perimeter

    def area(self):
        """method that returns the area of a rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """method that returns a rectangle characters"""
        if self.__height == 0 or self.__width == 0:
            return ""
        rec = ""
        for col in range(self.__height):
            for row in range(self.__width):
                rec += str(self.print_symbol)
            if col < self.__height - 1:
                rec += "\n"
        return rec

    def __repr__(self):
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    def bigger_or_equal(rect_1, rect_2):
        """method that returns the bigger rectangle
        Args:
            rect_1: first rectangle
            rect_2: second rectangle
        Raises:
            TypeError:if rect_1 or rect_2 are not instance of Rectangle
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
