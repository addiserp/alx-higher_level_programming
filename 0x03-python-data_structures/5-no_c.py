#!/usr/bin/python3
# a function that removes all characters c and C from a string.
def no_c(my_string):
    new = ''
    for i in my_string:
        if i != 'c' and i != 'C':
            new = new + i
    return new
