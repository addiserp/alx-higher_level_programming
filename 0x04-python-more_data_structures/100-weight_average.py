#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    re = 0.0
    slst = list(t[0] * t[1] for t in my_list)
    wlst = list(t[1] for t in my_list)
    re = sum(slst) / sum(wlst)
    return re
