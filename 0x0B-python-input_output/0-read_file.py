#!/usr/bin/python3
"""a function that reads a text file (UTF8)
and prints it to stdout:"""


def read_file(filename=""):
    """a function that reads a text file (UTF8)"""

    with open(filename, mode='r', encoding="utf-8") as myfile:
        myread = myfile.read()
        print(myread)
