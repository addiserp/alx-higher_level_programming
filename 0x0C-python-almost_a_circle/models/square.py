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
        self.__x = x
        self.integer_validator2("y", y)
        self.__y = y

    @property
    def size(self):
        """Gets value of size"""
        return self.__width

    @size.setter
    def size(self, value):
        """assign a value size"""

        if self.width == self.height:
            self.integer_validator("size", value)
        self.height = value
        self.width = value

    def __str__(self) -> str:
        """presents a diagram of the square defined for an object"""

        name = str(self.__class__.__name__)
        printstr = "[{}] ({}) {}/{} - {}"
        return printstr.format(name, self.id,
                               self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """updates the square instance"""

        if len(args) == 0:
            for key, val in kwargs.items():
                self.__setattr__(key, val)
            return

        strcont = len(args) - 1
        if strcont >= 0:
            self.id = args[0]
        if strcont >= 1:
            self.size = args[1]
        if strcont >= 2:
            self.x = args[2]
        if strcont >= 3:
            self.y = args[3]

    def to_dictionary(self):
        """Dictionary representation of the class Square"""

        return {'id': getattr(self, "id"),
                'x': getattr(self, "x"),
                'size': getattr(self, "width"),
                'y': getattr(self, "y")}
