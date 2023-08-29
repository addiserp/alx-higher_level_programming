#!/usr/bin/python3
# a function that returns the weighted average
# of all integers tuple (<score>, <weight>)
def weight_average(my_list=[]):
    if not my_list:
        return 0
    outp = 0.0
    slst = list(t[0] * t[1] for t in my_list)
    wlst = list(t[1] for t in my_list)
    outp = sum(slst) / sum(wlst)
    return outp
