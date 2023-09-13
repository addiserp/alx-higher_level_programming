#!/usr/bin/python3
"""a function that returns an object
(Python data structure) represented by a JSON string:"""
import json


def from_json_string(my_str):
    x = json.dumps(my_str)
    return json.loads(x)
