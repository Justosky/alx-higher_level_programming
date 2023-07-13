#!/usr/bin/python3

"""The definition of a text file raeding function """


def read_file(filename=""):
    with open(filename, 'r', encoding='UTF-8') as file:
        print(file.read(), end="")
