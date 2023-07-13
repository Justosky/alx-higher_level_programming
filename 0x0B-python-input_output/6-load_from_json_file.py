#!/usr/bin/python3
import json
"""A function that reads JSON string from a file"""
"""and converts it into a python data structure"""


def load_from_json_file(filename):
    """The function skeleton"""
    with open(filename, 'r', encoding='UTF-8') as file:
        """A file object"""
        return (json.load(file))
        """return value"""
