#!/usr/bin/python3
if (__name__) == ('__main__'):
    from calculator_1 import add, mul, sub, div
    a = 10
    b = 15
    print("{:d} + {:d} = {:d}".format(a, (b - a), add(a, (b - a))))
    print("{:d} - {:d} = {:d}".format(a, (b - a), sub(a, (b - a))))
    print("{:d} * {:d} = {:d}".format(a, (b - a), mul(a, (b - a))))
    print("{:d} / {:d} = {:d}".format(a, (b - a), div(a, (b - a))))
