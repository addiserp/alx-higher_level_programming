#!/usr/bin/python3
"""
a Module that prints 2 new lines after ".?:"
"""


def text_indentation(text):
    """ a module that prints 2 new lines after ".?:" characters
    Args:
        text: input string
    Returns:
        Nothing.
    Raises:
        TypeError: If text is not a string
    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    str1 = text[:]

    for i in ".?:":
        list_text = str1.split(i)
        str1 = ""
        for j in list_text:
            j = j.strip(" ")
            str1 = j + i if str1 is "" else str1 + "\n\n" + j + i

    print(str1[:-3], end="")
