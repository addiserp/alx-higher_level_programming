#!/usr/bin/python3

"""a function that returns True if the object is exactly
an instance of the specified class ; otherwise False."""


def is_same_class(obj, a_class):
    """ a is_same_class cheaker function"""
    if type(obj) == a_class:
        return True
    else:
        return False
