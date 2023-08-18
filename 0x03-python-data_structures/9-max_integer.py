#!/usr/bin/python3
# a function that finds the biggest integer of a list
def max_integer(my_list=[]):
    size = len(my_list)
    if size == 0:
        return "None"
    else:
        max = my_list[0]
        for i in range(size):
            if max < my_list[i]:
                max = my_list[i]
        return max
