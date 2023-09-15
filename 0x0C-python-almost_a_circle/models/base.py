#!/usr/bin/python3
""" My class Base module
"""


class Base:
    """ The first class Base
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """initialize the new class"""

        """Args:
                id (int): The identity of the new Base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    def __str__(self):
        return "[Base] {} - {:d}".format(self.id)
