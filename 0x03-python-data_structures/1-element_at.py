#!/usr/bin/python3
# 0x03-python-data_structures
# a function that retrieves an element from a list like in C.
def element_at(my_list, idx):
    if idx < 0 :
        return
    elif idx > len(my_list) - 1:
        return
    else:
        return my_list[idx]
    