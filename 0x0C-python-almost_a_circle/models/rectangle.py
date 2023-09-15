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
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
        self.integer_validator2("x", x)
        self.__x = x
        self.integer_validator2("y", y)
        self.__y = y

    @property
    def width(self):
        """retrieves width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets width attribute"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """retrieves height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets height attribute"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """retrieves x attribute"""
        return self.__x

    @x.setter
    def x(self, value):
        """sets x attribute"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value <= 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """retrieves x attribute"""
        return self.__x

    @y.setter
    def y(self, value):
        """sets y attribute"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value <= 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def integer_validator(self, name, value):
        """validates value"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

    def integer_validator2(self, name, value):
        """validates value for x & y"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value < 0:
            raise ValueError("{} must be >= 0".format(name))

    def area(self):
        """Returns the area of the rectangle"""
        return (self.__width * self.__height)

    def display(self):
        """Displays in # patern"""
        rectangle = ""
        print("\n" * self.y, end="")
        for i in range(self.height):
            rectangle += (" " * self.x) + ("#"*self.width) + "\n"
        print(rectangle, end="")
