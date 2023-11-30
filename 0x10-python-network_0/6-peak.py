#!/usr/bin/python3
"""
    function that finds a peak in a list of unsorted integers.
"""


def find_peak(num):
    '''
        will Find the peak in a list of unsorted numbers
    '''
    unleng = len(num)
    if unleng == 0:
        return None
    if unleng == 1:
        return (num[0])
    if unleng == 2:
        return num[0] if num[0] >= num[1] else num[1]

    for idx in range(0, unleng):
        value = num[idx]
        if (idx > 0 and idx < unleng - 1 and
                num[idx + 1] <= value and num[idx - 1] <= value):
            return value
        elif idx == 0 and num[idx + 1] <= value:
            return value
        elif idx == unleng - 1 and num[idx - 1] <= value:
            return value
    return value
