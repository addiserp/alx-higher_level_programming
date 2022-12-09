#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for xx in list(a_dictionary.keys()):
        if a_dictionary[xx] == value:
            del a_dictionary[xx]
    return a_dictionary
