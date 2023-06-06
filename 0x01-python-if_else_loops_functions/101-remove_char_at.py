#!/usr/bin/python3
def remove_char_at(str, n):
    if (n < 0 or n >= len(str)):
        return (str)
    new_str = list(str)
    new_str = new_string.pop(n)
    new_string = " ".join(new_str)
    return (new_string)
