#!/usr/bin/python3
# a function that deletes the item at a specific position in a list.
def delete_at(my_list=[], idx=0):
    size = len(my_list)
    temp_list = []
    if size == 0 or idx < 0 or idx > size - 1:
        return my_list
    del my_list[idx]
    return my_list
