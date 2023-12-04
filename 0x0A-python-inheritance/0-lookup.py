#!/usr/bin/python3

"""lockup module"""


def lookup(obj):
    """function that returns the list of availble attributes and
        methods of an object.

        Args:
            obj: method or object.
    """
    return (dir(obj))
