#!/usr/bin/python3

'''
This function(number_keys) takes a dictionary as
the only argument.  it initializes a variable count
to 0 it itereate over the the dictionary using a temporary
variable and a for loop. For each iteration the count is incremented.
The function later returns count which is the value for the number of
keys that the dictonary contains.
'''


def number_keys(a_dictionary):
    count = 0
    for _ in a_dictionary:
        count = count + 1
    return (count)
