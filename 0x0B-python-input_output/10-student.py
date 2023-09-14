#!/usr/bin/python3
""" a class Student that defines a student by
using 9-student.py
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

    def to_json(self, ats=None):
        """__str__ to_json"""
        if (type(ats) == list and
                all(type(ele) == str for ele in ats)):
            return {k: getattr(self, k) for k in ats if hasattr(self, k)}
        return self.__dict__
