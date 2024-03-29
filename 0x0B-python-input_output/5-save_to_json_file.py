#!/usr/bin/python3
"""a function that writes an Object to
a text file, using a JSON representation"""
import json


def save_to_json_file(my_obj, filename):
    """a function that writes an Object to"""

    with open(filename, mode="+w", encoding="utf-8") as myfile:
        j = json.dumps(my_obj)
        count = myfile.write(j)
