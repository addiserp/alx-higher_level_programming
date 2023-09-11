#!/usr/bin/python3
"""Defines a Circle inherits from Rectangel"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """a class Square that inherits from (9-rectangle.py)."""
    __size = 0

    def __init__(self, size):

        """a function Rectangle that intialize width & height."""
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """Get the area of a Square
        Returns: The size squared
        """
        return self.__size * self.__size

    def perimeter(self):
        """Returns the perimeter of the square"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self) -> str:
        """presents a diagram of the square defined for an object"""

        Square = "[Square] {}/{}".format(self.__size, self.__size)
        return (Square)
