#!/usr/bin/python3
"""Unittests for max_integer([..])."""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Define unittests for max_integer([..])."""

    def test_ordered_list(self):
        """ordered list of integers."""
        ordered = [5, 6, 7, 8]
        self.assertEqual(max_integer(ordered), 8)

    def test_unordered_list(self):
        """Test an unordered list of integers."""
        unordered = [6, 5, 7, 4]
        self.assertEqual(max_integer(unordered), 7)

    def test_max_at_begginning(self):
        """Test a list with a beginning max value."""
        max_at_beginning = [4, 3, 2, 1]
        self.assertEqual(max_integer(max_at_beginning), 4)

    def test_empty_list(self):
        """Test an empty list."""
        empty = []
        self.assertEqual(max_integer(empty), None)

    def test_one_element_list(self):
        """Test a list with a single element."""
        one_element = [7]
        self.assertEqual(max_integer(one_element), 7)

    def test_floats(self):
        """a list of floats Test."""
        floats = [14.32, 7.43, -14.13, 16.42, 5.5]
        self.assertEqual(max_integer(floats), 16.42)

    def test_ints_and_floats(self):
        """a list of ints and floats test."""
        ints_and_floats = [1.3, 5.5, -19, 5, 6]
        self.assertEqual(max_integer(ints_and_floats), 6)

    def test_string(self):
        """a string test."""
        string = "mikias"
        self.assertEqual(max_integer(string), 's')

    def test_list_of_strings(self):
        """a list of strings test."""
        strings = ["miki", "is", "my", "name"]
        self.assertEqual(max_integer(strings), "name")

    def test_empty_string(self):
        """an empty string test."""
        self.assertEqual(max_integer(""), None)

if __name__ == '__main__':
    unittest.main()
