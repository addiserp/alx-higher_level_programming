#!/usr/bin/python3
"""a script that adds all arguments to a Python list
, and then save them to a file:"""
import json
import sys
from os import path
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


filename = "add_item.json"
strcont = len(sys.argv) - 1
if strcont == 0:
    sys.exit(1)
else:
    my_list = []
    for i in range(strcont):
        my_list.append(sys.argv[i + 1])

if path.isfile(filename):
    """path checker if it exists"""

    curr_list = load_from_json_file(filename)
    save_to_json_file(curr_list + my_list, filename)

else:
    """path checker if it does not exists"""
    save_to_json_file(my_list, filename)
