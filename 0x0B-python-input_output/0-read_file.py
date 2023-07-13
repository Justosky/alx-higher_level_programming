#!/usr/bin/python3

"""
read_file: A function that reads the content of a file using UTF-8 encoding.
@filename: The name of the file which content is to be read.
"""


def read_file(filename=""):
    with open(filename, 'r', encoding='UTF-8') as file:
        for each_line in file:
            print(each_line, end="")
