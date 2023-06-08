#!/usr/bin/python3
if (__name__) == ("__main__"):
    result = 0
    from sys import argv
    count = (len(argv) - 1)
    for index in range(count):
        result = result + (int)(argv[index + 1])
    print("{}".format(result))
