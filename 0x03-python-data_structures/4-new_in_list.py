#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    length = (len(my_list) - 1)
    if idx < 0:
        return my_list.copy()
    elif idx > length:
        return my_list.copy()
    else:
        my_listcopy = my_list.copy()
        my_listcopy[idx] = element
        return my_listcopy
