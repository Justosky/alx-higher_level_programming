#!/usr/bin/python3

'''
This function (simple_delete) takes two
arguments a_dictionary and key
@a_dictionary: A dictionary.
@key: The key of the dictionary that we want to delete
The function checks if the key exis in the
dictionary and if  the statement evaluates to true
the function deletes the key along with it's value
out of the dictionary.
The function returns the uppdated dictionary.
'''


def simple_delete(a_dictionary, key=""):
    if key in a_dictionary:
        del a_dictionary[key]
    return (a_dictionary)
