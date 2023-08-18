#!/usr/bin/python3
# a function that returns a key with the biggest integer value.

def best_score(a_dictionary):

    if not a_dictionary:
        return None
    else:
        new_list = dict(sorted(a_dictionary.items()))
        big = 0
        for key, value in new_list.items():
            if value > big:
                keys = key
    return key
