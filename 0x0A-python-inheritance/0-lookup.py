#!/usr/bin/python3

"""a function that returns the list of available
attributes and methods of an object:"""


def lookup(obj):
    """ a lookup function"""
    nlist = []
    nlist = dir(obj)
    return nlist
