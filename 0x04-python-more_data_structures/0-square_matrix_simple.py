#!/usr/bin/python3
# a function that computes the square value of all integers of a matrix.
def square_matrix_simple(matrix=[]):
    new_matrix = []
    new_matrix = [list(map(lambda x: x ** 2, row)) for row in matrix]
    return new_matrix
