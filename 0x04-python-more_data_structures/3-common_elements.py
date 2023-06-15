#!/usr/bin/python3

def common_elements(set_1, set_2):
    return (set_1 &  set_2)
my_set1={1, 2, 10, 15, 20,100}
my_set2={2, 4, 10, 30, 15, 100}
x = common_elements(my_set1, my_set2)
print(x)
