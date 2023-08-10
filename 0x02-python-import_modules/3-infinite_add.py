#!/usr/bin/python3
# a program that prints the result of the addition of all arguments

if __name__ == "__main__":
    import sys
    strcont = len(sys.argv) - 1
    sum = 0
    for i in range(strcont):
        sum += int(sys.argv[i + 1])
    print(sum)

