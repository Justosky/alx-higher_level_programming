#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
LastDigit = number % 10
if (number < 0):
    LastDigit = (number * -1) % 10
    LastDigit = -1 * LastDigit
if (LastDigit == 0):
    print(f"Last digit of {number:d} is {LastDigit:d} and is 0")
elif (LastDigit > 5):
    print(f"Last digit of {number:d} is {LastDigit:d} and is greater than 5")
elif (LastDigit != 0 and LastDigit < 6):
    print(f"Last digit of {number} is", end=" ")
    print(f"{LastDigit:d} and is less than 6 and not 0")
