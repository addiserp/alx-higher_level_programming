#!/usr/bin/python3
# 0x03-python-data_structures
#  a function that replaces an element in a list
# at a specific position without modifying the original list (like in C).

def new_in_list(my_list, idx, element):
    new = my_list.copy()
    if idx < 0:
        return new
    elif idx > len(my_list) - 1:
        return new
    else:
        new[idx] = element
        return new
