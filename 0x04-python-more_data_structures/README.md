language: C
--
Number: 89
ids: [1, 2, 3]
language: C
guillaume@ubuntu:~/0x04$ 
Repo:

GitHub repository: alx-higher_level_programming
Directory: 0x04-python-more_data_structures
File: 8-simple_delete.py
   
9. Multiply by 2
mandatory
Write a function that returns a new dictionary with all values multiplied by 2

Prototype: def multiply_by_2(a_dictionary):
You can assume that all values are only integers
Returns a new dictionary
You are not allowed to import any module
guillaume@ubuntu:~/0x04$ cat 9-main.py
#!/usr/bin/python3
multiply_by_2 = __import__('9-multiply_by_2').multiply_by_2
print_sorted_dictionary = \
    __import__('6-print_sorted_dictionary').print_sorted_dictionary

a_dictionary = {'John': 12, 'Alex': 8, 'Bob': 14, 'Mike': 14, 'Molly': 16}
new_dict = multiply_by_2(a_dictionary)
print_sorted_dictionary(a_dictionary)
print("--")
print_sorted_dictionary(new_dict)

guillaume@ubuntu:~/0x04$ ./9-main.py
Alex: 8
Bob: 14
John: 12
Mike: 14
Molly: 16
--
Alex: 16
Bob: 28
John: 24
Mike: 28
Molly: 32
guillaume@ubuntu:~/0x04$ 
Repo:

GitHub repository: alx-higher_level_programming
Directory: 0x04-python-more_data_structures
File: 9-multiply_by_2.py
   
10. Best score
mandatory
Write a function that returns a key with the biggest integer value.

Prototype: def best_score(a_dictionary):
You can assume that all values are only integers
If no score found, return None
You can assume all students have a different score
You are not allowed to import any module
guillaume@ubuntu:~/0x04$ cat 10-main.py
#!/usr/bin/python3
best_score = __import__('10-best_score').best_score

a_dictionary = {'John': 12, 'Bob': 14, 'Mike': 14, 'Molly': 16, 'Adam': 10}
best_key = best_score(a_dictionary)
print("Best score: {}".format(best_key))

best_key = best_score(None)
print("Best score: {}".format(best_key))

guillaume@ubuntu:~/0x04$ ./10-main.py
Best score: Molly
Best score: None
guillaume@ubuntu:~/0x04$ 
Repo:

GitHub repository: alx-higher_level_programming
Directory: 0x04-python-more_data_structures
File: 10-best_score.py
   
11. Multiply by using map
mandatory
Write a function that returns a list with all values multiplied by a number without using any loops.

Prototype: def multiply_list_map(my_list=[], number=0):
Returns a new list:
Same length as my_list
Each value should be multiplied by number
Initial list should not be modified
You are not allowed to import any module
You have to use map
Your file should be max 3 lines
guillaume@ubuntu:~/0x04$ cat 11-main.py
#!/usr/bin/python3
multiply_list_map = __import__('11-multiply_list_map').multiply_list_map

my_list = [1, 2, 3, 4, 6]
new_list = multiply_list_map(my_list, 4)
print(new_list)
print(my_list)

guillaume@ubuntu:~/0x04$ ./11-main.py
[4, 8, 12, 16, 24]
[1, 2, 3, 4, 6]
guillaume@ubuntu:~/0x04$ 
Repo:

GitHub repository: alx-higher_level_programming
Directory: 0x04-python-more_data_structures
File: 11-multiply_list_map.py
   
12. Roman to Integer
mandatory
Technical interview preparation:

You are not allowed to google anything
Whiteboard first
Create a function def roman_to_int(roman_string): that converts a Roman numeral to an integer.

You can assume the number will be between 1 to 3999.
def roman_to_int(roman_string) must return an integer
If the roman_string is not a string or None, return 0
guillaume@ubuntu:~/0x04$ cat 12-main.py
#!/usr/bin/python3
""" Roman to Integer test file
"""
roman_to_int = __import__('12-roman_to_int').roman_to_int

roman_number = "X"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "VII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "IX"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "LXXXVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "DCCVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

guillaume@ubuntu:~/0x04$ ./12-main.py
X = 10
VII = 7
IX = 9
LXXXVII = 87
DCCVII = 707
guillaume@ubuntu:~/0x04$ 
Repo:

GitHub repository: alx-higher_level_programming
Directory: 0x04-python-more_data_structures
File: 12-roman_to_int.py
   
