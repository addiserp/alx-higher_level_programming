#!/usr/bin/python3
# a function that prints the first x elements of a list and only integers.
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    new_list = []
    for i in range(x):
        try:
            new_list[i] = my_list[i]
        except (IndexError):
            False
    return new_list
