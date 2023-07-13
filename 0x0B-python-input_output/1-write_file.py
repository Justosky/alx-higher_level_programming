#!/usr/bin/python3

"""The definition for a function that writes to a file"""


def write_file(filename="", text=""):
    """Function skeleton"""
    with open(filename, 'w', encoding="UTF-8") as file:
        """Create a file object"""
        return (file.write(text))
        """Return value"""
