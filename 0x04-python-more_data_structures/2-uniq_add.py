#!/usr/bin/python3

def uniq_add(my_list=[]):
    result = 0
    for any_number in set(my_list):
        result = result + any_number
    return (result)
