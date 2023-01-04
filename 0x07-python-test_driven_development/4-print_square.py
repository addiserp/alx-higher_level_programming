#!/usr/bin/python3
"""
This function that prints a square with the character #
"""


def print_square(size):
    """ this Function prints a square with the character #
    Args:
        size: size of the square.
    Returns:
        Nothing
    Raises:
        TypeError: If size is not an integer.
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
