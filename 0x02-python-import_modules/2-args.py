#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    count = (len(sys.argv) - 1)
    if (count == 0):
        print("{} arguments.".format(count))
    elif (count == 1):
        print("{} argument:\n{}: {}".format(count, count, sys.argv[count]))
    else:
        print("{} arguments:".format(count))
        for index in range(count):
            print("{}: {}".format((index + 1), sys.argv[index + 1]))
