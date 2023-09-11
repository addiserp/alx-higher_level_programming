#!/usr/bin/python3
# 7-base_geometry.py by Mikias Gedlu
"""Defines an empty class BaseGeometry """


class BaseGeometry:
    """Does nothing"""
    def area(self):
        """raises an Exception with the message
        area() is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value"""
        if type(value) is not int:
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
