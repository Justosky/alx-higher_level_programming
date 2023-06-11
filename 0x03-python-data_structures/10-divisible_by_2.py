#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    if my_list == []:
        return
    new_list = my_list.copy()
    for count in range(0,  len(my_list)):
        if (my_list[count] % 2 == 0):
            new_list[count] = 1
        else:
            new_list[count] = 0
    return (new_list)
