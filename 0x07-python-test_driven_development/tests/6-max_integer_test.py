#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_MaxIinteger(self):
        # Test starts with all integers
        self.assertAlmostEqual(max_integer([1, -2, 3, 4]),4)
        self.assertAlmostEqual(max_integer([1, 5, -3, 4]),5)
        self.assertAlmostEqual(max_integer([8, 5, 3, 4]),8)
    
  #def test_values(self):
        # Make sure value errors are raised when necessory
   #     self.assertRaises(ValueError,max_integer, [1, -2, 3, 4.7]) '''
    def test_Types(self):
        # Make sure value errors are raised when necessory
        self.assertRaises(TypeError,max_integer, [1, -2, 3, 4.7])
        self.assertRaises(TypeError,max_integer, [1, -2, 3, True])
        self.assertRaises(TypeError,max_integer, [1, -2, 3, "abc"])

if __name__ == '__main__':
    unittest.main()