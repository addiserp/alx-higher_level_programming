#!/usr/bin/python3
""" a class Student that defines a student by
"""


class Student:
    """ a class Student that defines a student by
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self):
        """__str__ documentation"""
        v = "{} - {} - {:d}".format(self.first_name, self.last_name, self.age)
        return "[Student] " + v

    def to_json(self):
        """__str__ to_json"""
        return self.__dict__
