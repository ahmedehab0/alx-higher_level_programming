#!/usr/bin/python3

"""append to a file module"""


def append_write(filename="", text=""):
    """function that appends a string to the end of a text file"""
    with open(filename, mode='a', encoding="utf-8") as f:
        return f.write(text)
