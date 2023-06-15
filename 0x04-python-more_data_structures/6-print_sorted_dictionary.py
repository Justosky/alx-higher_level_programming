#!/usr/bin/python3

'''
A function called (print_sorted_dictionary)
that takes a_dictionary
as the the only argument. In the for loop it sorts the key
in the dictionary using
the sorted function and stores each sorted key in the any_key variable.
It then prints
each sorted key stored in the any_key variable along with
the key value using
the string formatter.this function ensures that
the any_keys is handled as a string.
the function returns nothing
'''


def print_sorted_dictionary(a_dictionary):
    for any_key in sorted(a_dictionary.keys()):
        print("{:s}: {}".format(any_key, a_dictionary[any_key]))
