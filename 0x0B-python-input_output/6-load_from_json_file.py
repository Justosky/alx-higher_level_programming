#!/usr/bin/python3
"""A function that reads JSON string from a file"""
import json


def load_from_json_file(filename):
    """The function skeleton"""
    with open(filename, 'r', encoding='UTF-8') as file:
        """A file object"""
        return (json.load(file))
        """return value"""
