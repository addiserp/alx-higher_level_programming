#!/usr/bin/python3
""" My class Base module
"""
import json

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
        """ formats string reparezantation"""

        return "[Base] {} - {:d}".format(self.id)

    def to_json_string(list_dictionaries):
        """returns the JSON string representation
        of list_dictionaries:"""

        if list_dictionaries is None:
            return "[]"

        return json.dumps(list_dictionaries)
    