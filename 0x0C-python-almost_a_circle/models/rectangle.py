#!/usr/bin/python3
""" My class Rectangle module
"""
from models.base import Base


class Rectangle(Base):
    """ The first class REctangle inherits from Base
    """

    __width = 0
    __height = 0
    __x = 0
    __y = 0

    def __init__(self, width, height, x=0, y=0, id=None):
        """initialize the new class"""

        """Args:
                width (int): The width of the new rectangle.
                height (int): The height of the new rectangle.
                x (int): The x of the new rectangle.
                y (int): The y of the new rectangle.
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__y = y
        self.__x = x

    @property
    def width(self):
        """retrieves width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets width attribute"""
        self.__width = value

    @property
    def height(self):
        """retrieves height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets height attribute"""
        self.__height = value

    @property
    def x(self):
        """retrieves x attribute"""
        return self.__x

    @x.setter
    def x(self, value):
        """sets x attribute"""
        self.__x = value

    @property
    def y(self):
        """retrieves x attribute"""
        return self.__x

    @y.setter
    def y(self, value):
        """sets y attribute"""
        self.__y = value
