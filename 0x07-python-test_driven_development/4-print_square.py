#!/usr/bin/python3
"""
4-print_square.py, by Mikias Gedlu
This module is prints square in # format
"""


def print_square(size):

    """ print_square  in # format
    Args:
        size: size of square
    Returns:
        Nothing
    Raises:
        TypeError: size must be >= 0
        TypeError: size must be an integer
    """
    """presents a diagram of the rectangle defined for an object"""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise TypeError("size must be >= 0")
    square = ""
    for column in range(size):
        for row in range(size):
            square += "#"
            if row > size - 2:
                square += "\n"
    print(square)
