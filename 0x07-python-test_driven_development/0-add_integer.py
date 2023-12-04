#!/usr/bin/pyhton3

"""add integer module"""

def add_integer(a, b=98):
    """function that adds two integers
        Args:
            a: first integer
            b:second integer
        Raises:
            TypeError if a or b are not intgers 
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
