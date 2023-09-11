#!/usr/bin/python3
"""Defines a Rectangle inherits from """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """a class Rectangle that inherits from (7-base_geometry.py)."""

    def __init__(self, width, height):

        """a function Rectangle that intialize width & height."""
        if width is None or height is None:
            return
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
