#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    return [list(map((lambda number: number * number), num_in_matrix))
            for num_in_matrix in matrix]
