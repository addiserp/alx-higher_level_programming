#!/usr/bin/python3
""" function that creates an Object from a “JSON file"""
import json


def load_from_json_file(filename):
    """a function that creates an Object from a “JSON file"""

    with open(filename, mode="r", encoding="utf-8") as myfile:
        mylist = json.load(myfile)
        return mylist
