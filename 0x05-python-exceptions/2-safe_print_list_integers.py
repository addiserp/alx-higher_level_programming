#!/usr/bin/python3
# a function that prints the first x elements of a list and only integers.
def safe_print_list_integers(my_list=[], x=0):
    for i in range(0,x):
        try:
            if type(list[i] == int):
                print("{:d}".format(list[i]))
        except:
            return False
