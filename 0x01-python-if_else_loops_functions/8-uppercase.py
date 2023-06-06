#!/usr/bin/python3
def uppercase(str):
    for each_character in str:
        if (ord(each_character) >= 97 and ord(each_character) <= 122):
            each_character = each_character - 32
        print("{:s}".format(each_character), end="")
    print("\n", end="")
