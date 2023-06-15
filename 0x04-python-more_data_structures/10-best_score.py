#!/usr/bin/python3

'''
A function that returns the key in a dictionary with the maximum  interger
returns none if the dictionary is empty or does not exist.
this function assumes that all  values for keys in the dictionary contains
an interger value.
'''


def best_score(a_dictionary):
    if a_dictionary and len(a_dictionary):
        return (None)
    else:
        max_key = list(a_dictionary.keys())[0]
        for any_key in a_dictionary:
            if a_dictionary[any_key] > dictionary[max_key]
            max_key = any_key
        return (max_key)
