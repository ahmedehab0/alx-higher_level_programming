#!/usr/bin/python3

"""save to JSON module"""


import json


def save_to_json_file(my_obj, filename):
    """function writes an Object to a text file, using a JSON representation"""
    with open(filename, mode='w', encoding="utf-8") as f:
        json.dump(my_obj, f)
