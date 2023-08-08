#!/usr/bin/python3
# a function that prints the last digit of a number

def print_last_digit(n):
    if n < 0:
        lst = n % -10
    else:
        lst = n % 10
    i = abs(lst)
    print("{}".format(i), end="")
    return i
