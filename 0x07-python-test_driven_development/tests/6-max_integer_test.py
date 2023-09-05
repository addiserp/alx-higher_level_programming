#!/usr/bin/python3
"""a test Module for 6-max_integer.py to find the max integer in a list
"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class Testmax_integer(unittest.TestCase):
    def test_MaxIinteger(self):
        # test max integer when integers
        self.assertAlmostEqual(max_integer([1, -2, 3, 4]),4)
        self.assertAlmostEqual(max_integer([1, 5, -3, 4]),5)
        self.assertAlmostEqual(max_integer([8, 5, 3, 4]),8)

    def test_Types(self):
        # make sure value errors are raized
        self.assertRaises(TypeError, max_integer, [1, 2, 3, -4, False])
        self.assertRaises(TypeError, max_integer, [1, 2, 3, 2.4, "a"])

        self.assertRaises(TypeError,max_integer, [1, -2, 3, 4.7])
        self.assertRaises(TypeError,max_integer, [1, -2, 3, True])
        self.assertRaises(TypeError,max_integer, [1, -2, 3, "abc"])
