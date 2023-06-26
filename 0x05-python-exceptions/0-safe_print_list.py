#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    count = 0


try:
    for any_num in range(x):
        print(my_list[any_num], end="")
        count = count + 1
    print()
    return (count)
except IndexError:
    print()
    return (count)
