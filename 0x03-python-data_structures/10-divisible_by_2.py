#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    newlst = []
    for i in my_list:
        if i % 2 == 0:
            newlst.append(True)
        else:
            newlst.append(False)
    return (newlst)
