#!/usr/bin/python3

"""The definition of a text file raeding function"""


def read_file(filename=""):
    """Function prototype"""
    with open(filename, 'r', encoding='UTF-8') as file:
        """Creates a file object"""
        print(file.read(), end="")
        """Prints the contents of the file"""
