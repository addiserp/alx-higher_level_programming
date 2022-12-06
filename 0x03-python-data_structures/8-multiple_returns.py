#!/usr/bin/python3

def multiple_returns(sentence):
    if sentence != '':
        f1char = sentence[0]
    else:
        f1char = None
    return (len(sentence), f1char)
