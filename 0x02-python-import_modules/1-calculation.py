#!/usr/bin/python3
from calculator_1 import add as add
from calculator_1 import sub as sub
from calculator_1 import mul as mul
from calculator_1 import div as div
a = 10
b = 5
print('{:d} + {:d} = {:d}'.format(a, b, add(a, b)))
print('{:d} - {:d} = {:d}'.format(a, b, sub(a, b)))
print('{:d} * {:d} = {:d}'.format(a, b, mul(a, b)))
print('{:d} / {:d} = {:d}'.format(a, b, div(a, b)))
