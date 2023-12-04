#!/usr/bin/python3

"""module that defines a function that add attributes to an object"""


def add_attribute(obj, name, value):
    """function that adds a new attribute to an object if it’s possible"""

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, name, value)
