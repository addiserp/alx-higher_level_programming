#!/usr/bin/python3
# 6-base_geometry.py by Mikias Gedlu
"""Defines an empty class BaseGeometry """


class BaseGeometry:
    """Does nothing"""
    def area(self):
        """raises an Exception with the message 
        area() is not implemented"""
        raise TypeError("area() is not implemented")
