#!/usr/bin/python3
"""JSON string to python data structure converter function"""
import json


def from_json_string(my_str):
    """Function prototype"""
    return (json.loads(my_str))
    """return a python data structure"""
