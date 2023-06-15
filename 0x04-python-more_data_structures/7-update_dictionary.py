#!/usr/bin/python3

'''
This function called update_dictionary takes
three arguments a_dictionary, key and value.
It changes the value of a given key of a_dictionary with the given value.
@a_dictionary:  the dictionary that we are working with
@key: The key of the dictionary that we want to update
@value: The value that we want to assign to the key of
a_dictionary.
This function returns the newly updated a_dictionary
'''


def update_dictionary(a_dictionary, key, value):
    a_dictionary[key] = value
    return (a_dictionary)
