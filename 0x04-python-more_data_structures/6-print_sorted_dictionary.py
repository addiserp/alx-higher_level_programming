#!/usr/bin/python3
# a function that prints a dictionary by ordered keys.
def print_sorted_dictionary(a_dictionary):
    new_list = {}
    new_list = sorted(a_dictionary.items())
    for key, value in new_list:
        print("{}: {}".format(key, value))
