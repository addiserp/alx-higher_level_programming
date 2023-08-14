#!/usr/bin/python3
# a function that prints a matrix of integers.
def print_matrix_integer(matrix=[[]]):
    for i in matrix[:]:
        for j in matrix[:]:
            print("{:d} ".format([i][j]))
