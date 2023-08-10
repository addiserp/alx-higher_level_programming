#!/usr/bin/python3
#a program that prints the number of and the list of its arguments.

if __name__ == "__main__":
    import sys
    strcont = len(sys.argv) - 1
    if strcont == 0:
        print("0 arguments.")
    elif strcont == 1:
        print("1 argument.")
    else:
        print("{} arguments:".format(strcont))
    for i in range(strcont):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
