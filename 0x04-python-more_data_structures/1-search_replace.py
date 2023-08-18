#!/usr/bin/python3
# a function that replaces all occurrences
# of an element by another in a new list.
# my_list is the initial list
# search is the element to replace in the list
# replace is the new element

def search_replace(my_list, search, replace):
    new_list = []
    for x in my_list:
        if x == search:
            new_list.append(replace)
        else:
            new_list.append(x)
    return new_list
