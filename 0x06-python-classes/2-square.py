#!/usr/bin/python3
# 2-square.py by Mikias Gedlu
"""Defines a square """

class Square:
    """Does Define Square"""
    def __init__(self, size=0):
        """ a Module divides the numbers of a matrix
        Args: Size - size of square
        Returns:
            Nothing
        Raises:
            TypeError : size must be an integer
            ValueError : size must be >= 0
        """

        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
