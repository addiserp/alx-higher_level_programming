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

    @classmethod
    def save_to_file(cls, list_objs):
        """Save json to a file """

        filename = str(cls.__name__) + ".json"
        with open(filename, mode="w", encoding="utf-8") as myfile:
            if list_objs is None:
                j = ""
            else:
                list_objs = [o.to_dictionary() for o in list_objs]
                j = cls.to_json_string(list_objs)
            myfile.write(j)

    def from_json_string(json_string):
        """Load json to dictionary format"""

        if json_string is None:
            return "[]"
        else:
            return json.loads(json_string)
