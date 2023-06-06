#!/usr/bin/python3
def print_last_digit(number):
    LastDigit = number % 10
    if (number < 0):
        number = number * -1
        LastDigit = number % 10
    print(f"{LastDigit}", end="")
    return (LastDigit)
