#!/usr/bin/python3
# a function that prints a matrix of integers.
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for j in i:
            if j == i[-1]:
                print('{:d}'.format(j), end='')
            else:
                print('{:d}'.format(j), end=' ')
        print()
