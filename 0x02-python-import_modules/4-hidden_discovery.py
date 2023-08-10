#!/usr/bin/python3
if __name__ == "__main__":
    from hidden_4 import *

    listname = dir(hidden_4)
    for i in listname:
        if i[:2] != "__":
            print(i)
