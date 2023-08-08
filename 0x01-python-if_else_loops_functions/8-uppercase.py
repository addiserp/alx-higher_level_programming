#!/usr/bin/python3
# change to Uppercase
def uppercase(str):
    for i in range(len(str)):
        j = ord(str[i])
        if j >= 97 and j <= 122:
            j = j - 32
        print("{}".format(chr(j)), end="")
    print()
