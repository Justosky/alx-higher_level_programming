#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    answer_list = []
    for any_num in range(list_length):
        try:
            answer = my_list_1[any_num] + my_list_2[any_num]
        except (ValueError, TypeError):
            print("wrong type")
            answer = 0
        except (ZeroDivisionError):
            print("division by 0")
            answer = 0
        except (IndexError):
            print("out of range")
            answer = 0
        finally:
            answer_list.append(answer)
    return (answer_list)
