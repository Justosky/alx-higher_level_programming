#!/usr/bin/python3

'''
This function multiplies any all key values in a dictionary by two and
returns the updated dictionary.
'''


def multiply_by_2(a_dictionary):
    for any_key in a_dictionary:
        a_dictionary[any_key] = a_dictionary[any_key] * 2
    return (a_dictionary)
