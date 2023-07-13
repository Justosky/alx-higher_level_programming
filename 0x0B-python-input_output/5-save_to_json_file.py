#!/usr/bin/python3
"""A function that saves an object as a JSON string"""
import json


def save_to_json_file(my_obj, filename):
    """Function skeleton"""
    with open(filename, 'w', encoding='UTF-8') as file:
        """A file object"""
        return (json.dump(my_obj, file))
    """return the saved json string"""
