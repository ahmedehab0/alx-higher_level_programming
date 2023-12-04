#!/usr/bin/python3

"""load from JSON file module"""


import json


def load_from_json_file(filename):
    """function that creates an OBJECT from JSON file"""
    with open(filename, mode='r', encoding='utf-8') as f:
        return json.load(f)
