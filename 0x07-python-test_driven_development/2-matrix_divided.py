#!/usr/bin/python3
"""
2-matrix_divided.py by Mikias Gedlu
This module divides the numbers of a matrix
"""


def matrix_divided(matrix, div):
    """ a Module divides the numbers of a matrix
    Args:
        matrix: lists of integers/floats
        div: divides the matrix
    Returns:
        A new matrix with the result
    Raises:
        TypeError: If they aren't lists
                   If the lists aren't integers or floats
                   If div is not an integer float number
                   If they don't have the same size
        ZeroDivisionError: If the divider is zero
    """

    if not type(div) in (int, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")
    msg_type = "matrix must be a matrix (list of lists) of integers/floats"

    if not matrix or not isinstance(matrix, list):
        raise TypeError(msg_type)
    len_e = 0
    msg_size = "Each row of the matrix must have the same size"
    for elems in matrix:
        if not elems or not isinstance(elems, list):
            raise TypeError(msg_type)
        if len_e != 0 and len(elems) != len_e:
            raise TypeError(msg_size)
        for num in elems:
            if not type(num) in (int, float):
                raise TypeError(msg_type)
        len_e = len(elems)
    m = list(map(lambda x: list(map(lambda y: round(y / div, 2), x)), matrix))
    return (m)
