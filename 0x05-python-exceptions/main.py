#!/usr/bin/python3

print("This program prints an error message input is not an interger")
x = input("Please enter a number ")
try:
    x = int(x)
except (ValueError, TypeError) as x:
    import sys
print("Exception: {:s}".format(x), file=sys.stderr)
