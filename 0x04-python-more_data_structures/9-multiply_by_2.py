#!/usr/bin/python3

'''
This function multiplies any all key values in a dictionary by two and
returns the updated dictionary.
'''


def multiply_by_2(my_dict):
    return {any_key: any_value * 2 for any_key, any_value in my_dict.items()}
