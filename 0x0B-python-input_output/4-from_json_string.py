#!/usr/bin/python3

"""from json module"""


import json


def from_json_string(my_str):
    """function that returns a python object"""
    return json.loads(my_str)
