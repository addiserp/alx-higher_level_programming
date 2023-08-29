#!/usr/bin/python3
# 5-square.py by Mikias Gedlu
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

    def area(self):
        """
        Calculate area of the square
        Returns: The square of the size
        """
        return (self.__size ** 2)

    @property
    def size(self):
        """Retrieves size of square"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def my_print(self):
        """
        Prints area of the square in #
        """
        if self.__size == 0:
            print()
        for i in range(self.__size):
            print("#" * self.__size)
