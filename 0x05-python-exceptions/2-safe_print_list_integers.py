#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
count = 0
    for any_num in range(x):
        try:
            print("{:d}".format(my_list(any_num)))
            return (True)
        except (ValueError, TypeError)
            continue
    print()
    return (count)
