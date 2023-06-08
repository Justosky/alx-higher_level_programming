#!/usr/bin/python3
import calculator_1
a = 10
b = 15
if (__name__) == ('__main__'):
    print("{} + {} = {}".format(a, (b - a), calculator_1.add(a, (b - a))))
    print("{} - {} = {}".format(a, (b - a), calculator_1.sub(a, (b - a))))
    print("{} * {} = {}".format(a, (b - a), calculator_1.mul(a, (b - a))))
    print("{} / {} = {}".format(a, (b - a), calculator_1.div(a, (b - a))))
