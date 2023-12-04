#!/usr/bin/python3

"""file reading moudle"""


def read_file(filename=""):
    """function that reads a text from a file and print it to stdout"""

    with open(filename, encoding="utf-8") as f:
        file_data = f.read()
        print(file_data, end="")
