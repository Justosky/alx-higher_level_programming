#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv

if __name__ == "__main__":
    count = len(argv) - 1
    if count != 3:
        print("Usage: {:s} <a> <operator> <b>".format(argv[0]))
        exit(1)

    a = int(argv[1])
    operator = argv[2]
    b = int(argv[3])

    if operator == "+":
        answer = add(a, b)
        print("{} + {} = {}".format(a, b, answer))
    elif operator == "-":
        answer = sub(a, b)
        print("{} - {} = {}".format(a, b, answer))
    elif operator == "*":
        answer = mul(a, b)
        print("{} * {} = {}".format(a, b, answer))
    else:
        print("Unknown operator. Available operators: +, -, *")
        exit(1)
