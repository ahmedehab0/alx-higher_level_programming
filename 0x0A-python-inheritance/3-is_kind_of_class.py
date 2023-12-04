#!/usr/bin/python3

"""module that defines a class checking function"""


def is_kind_of_class(obj, a_class):
    """function that checks if the object is an instance of, or if the object
    is an instance of a class that inherited from, the specified class
    """

    return (isinstance(obj, a_class))
