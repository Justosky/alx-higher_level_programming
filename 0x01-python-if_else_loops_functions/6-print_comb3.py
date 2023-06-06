#!/usr/bin/python3
for FirstDigit in range(0, 8):
    for SecondDigit in range(FirstDigit + 1, 10):
        print("{}".format(FirstDigit), end="")
        print("{}".format(SecondDigit), end=", ")
print("{:d}{:d}".format(FirstDigit + 1, SecondDigit))
