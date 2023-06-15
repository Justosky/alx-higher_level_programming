#!/usr/bin/python3

'''
A function called only_diff_elements that takes two
sets(set_1 and set_2) as arguments.
The function returns a new set which contains all elements
either in set_1 or set_2 but not in
both sets.
'''


def only_diff_elements(set_1, set_2):
    return (set_1 ^ set_2)
