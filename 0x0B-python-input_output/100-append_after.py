#!/usr/bin/python3
"""a function that inserts a line of text to a file,
after each line containing a specific string (see example):"""


def append_after(filename="", search_string="", new_string=""):
    """a function that inserts a line of text to a file
    """
    mystr = ""
    with open(filename, mode="r", encoding="utf-8") as myfile:
        for line in myfile:
            mystr += line
            if search_string in line:
                mystr += new_string
    with open(filename, mode="w", encoding="utf-8") as myfile2:
        myfile2.write(mystr)
