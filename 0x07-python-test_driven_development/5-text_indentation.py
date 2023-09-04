#!/usr/bin/python3
"""
5-text_indentation.py, by Mikias Gedlu
a function that prints a text with 2 new lines
after each of these characters: ., ? and :
"""


def text_indentation(text):

    """ ach of these characters:
    Args:
        text: text to be indented
    Returns:
        Nothing
    Raises:
        TypeError: if value not string
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    str1 = text[:]

    for i in ".?:":
        list_text = str1.split(i)
        str1 = ""
        for j in list_text:
            j = j.strip(" ")
            str1 = j + i if str1 is "" else str1 + "\n\n" + j + i

    print(str1[:-3], end="")
