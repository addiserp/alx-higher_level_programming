#!/usr/bin/python3
# 0x03-python-data_structures
# a function that replaces an element of a list at a specific position (like in C).
def replace_in_list(my_list, idx, element):
    if idx < 0 :
        return my_list
    elif idx > len(my_list) - 1:
        return my_list
    else:
        my_list[idx] = element
        return my_list
    