#!/usr/bin/python3

"""wrtie to a file module"""


def write_file(filename="", text=""):
    """function that wrties a string to a textfile"""

    with open(filename, mode='w', encoding="utf-8") as f:
        return f.write(text)
