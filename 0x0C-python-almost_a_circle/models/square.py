#!/usr/bin/python3
""" My class Square inherits from Rectangle module
"""
from models.rectangle import Rectangle
import sys


class Square(Rectangle):
    """ The second class Square inherits from Rectangle
    """

    def __init__(self, size, x=0, y=0, id=None):
        """intialize Square class"""

        """Args:
                id (int): The id instance of square.
                size (int): The height/width of the new square.
                x (int): The x of the new square.
                y (int): The y of the new square.
        """
        super().__init__(size, size, x, y, id)
        self.integer_validator("size", size)
        self.__width = size
        self.__height = size
        self.integer_validator2("x", x)
        self.__x = super().x
        self.integer_validator2("y", y)
        self.__y = super().y
