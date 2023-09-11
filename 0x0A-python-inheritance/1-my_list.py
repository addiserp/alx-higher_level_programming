#!/usr/bin/python3
# 1-my_list.py by Mikias Gedlu
"""Defines a class MyList that inherits from list"""


class MyList(list):
    """this represents MyList"""

    def print_sorted(self):
        """this represents print_sorted"""
        newlist = sorted(self)
        print(newlist)
