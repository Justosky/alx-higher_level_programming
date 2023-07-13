#!/usr/bin/python3

"""The defnition of a function that appends a string"""
"""at the end of a file"""


def append_write(filename="", text=""):
    """Function prototype"""
    with open(filename, 'a', encoding="UTF-8") as file:
        """Creates a file object"""
        return(file.write(text))
