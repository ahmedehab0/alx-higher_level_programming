#!/usr/bin/python3

"""module that define a function to check inhertetion"""


def inherits_from(obj, a_class):
    """function that checks  if the object is an instance of a class
    that inherited (directly or indirectly) from the specified class
    """

    return (issubclass(type(obj), a_class) and type(obj) is not a_class)
