#!/usr/bin/python3
#a function that prints the last digit of a number

def print_last_digit(n):
    if n < 0:
        l = n % -10
    else:
        l = n % 10
    i = abs(l)
    print("{}".format(i), end="")
    return i
