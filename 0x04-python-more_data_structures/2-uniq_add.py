#!/usr/bin/python3
# a function that adds all unique integers in a list
# (only once for each integer).
def uniq_add(my_list=[]):
    new_list = set(my_list)
    sum = 0
    for x in new_list:
        sum += x
    return sum
