#!/usr/bin/python3

"""Defines unittests for models/square.py.
Unittest classes:
    TestSquare_to_dictionary - 640
    TestSquare_update_kwargs - line 538
    TestSquare_update_args - line 426
    TestSquare_stdout - line 343
    TestSquare_area - line 322
    TestSquare_instantiation - line 24
    TestSquare_size - line 88
    TestSquare_x - line 166
    TestSquare_y - line 238
    TestSquare_order_of_initialization - line 306
"""
import io
import sys
import unittest
from models.base import Base
from models.square import Square


class TestSquare_instantiation(unittest.TestCase):
    """Below are a unittests for testing instantiation of the Square class."""

    def test_is_base(self):
        self.assertIsInstance(Square(10), Base)

    def test_is_rectangle(self):
        self.assertIsInstance(Square(10), Square)

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Square()

    def test_one_arg(self):
        y1 = Square(10)
        y2 = Square(11)
        self.assertEqual(y1.id, y2.id - 1)

    def test_two_args(self):
        y1 = Square(10, 2)
        y2 = Square(2, 10)
        self.assertEqual(y1.id, y2.id - 1)

    def test_three_args(self):
        y1 = Square(10, 2, 2)
        y2 = Square(2, 2, 10)
        self.assertEqual(y1.id, y2.id - 1)

    def test_four_args(self):
        self.assertEqual(7, Square(10, 2, 2, 7).id)

    def test_more_than_four_args(self):
        with self.assertRaises(TypeError):
            Square(1, 2, 3, 4, 5)

    def test_size_private(self):
        with self.assertRaises(AttributeError):
            print(Square(10, 2, 3, 4).__size)

    def test_size_getter(self):
        self.assertEqual(5, Square(5, 2, 3, 9).size)

    def test_size_setter(self):
        y = Square(4, 1, 9, 2)
        y.size = 8
        self.assertEqual(8, y.size)

    def test_width_getter(self):
        y = Square(4, 1, 9, 2)
        y.size = 8
        self.assertEqual(8, y.width)

    def test_height_getter(self):
        y = Square(4, 1, 9, 2)
        y.size = 8
        self.assertEqual(8, y.height)

    def test_x_getter(self):
        self.assertEqual(0, Square(10).x)

    def test_y_getter(self):
        self.assertEqual(0, Square(10).y)


class TestSquare_size(unittest.TestCase):
    """Below are a unittests for testing size initialization of the Square class."""

    def test_None_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(None)

    def test_str_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("invalid")

    def test_float_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(5.5)

    def test_complex_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(complex(5))

    def test_dict_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square({"a": 1, "b": 2}, 2)

    def test_bool_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(True, 2, 3)

    def test_list_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square([1, 2, 3])

    def test_set_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square({1, 2, 3}, 2)

    def test_tuple_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square((1, 2, 3), 2, 3)

    def test_frozenset_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(frozenset({1, 2, 3, 1}))

    def test_range_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(range(5))

    def test_bytes_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(b'Python')

    def test_bytearray_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(bytearray(b'abcdefg'))

    def test_memoryview_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(memoryview(b'abcdefg'))

    def test_inf_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(float('inf'))

    def test_nan_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(float('nan'))

    # Test size values
    def test_negative_size(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-1, 2)

    def test_zero_size(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0, 2)


class TestSquare_x(unittest.TestCase):
    """Below are a unittests for testing initialization of Square x attribute."""

    def test_None_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, None)

    def test_str_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, "invalid")

    def test_float_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, 5.5)

    def test_complex_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, complex(5))

    def test_dict_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, {"a": 1, "b": 2}, 2)

    def test_bool_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, True)

    def test_list_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, [1, 2, 3])

    def test_set_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, {1, 2, 3})

    def test_tuple_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, (1, 2, 3))

    def test_frozenset_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, frozenset({1, 2, 3, 1}))

    def test_range_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, range(5))

    def test_bytes_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, b'Python')

    def test_bytearray_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, bytearray(b'abcdefg'))

    def test_memoryview_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, memoryview(b'abcedfg'))

    def test_inf_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, float('inf'), 2)

    def test_nan_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, float('nan'), 2)

    def test_negative_x(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(5, -1, 0)


class TestSquare_y(unittest.TestCase):
    """Below are a unittests for testing initialization of Square y attribute."""

    def test_None_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 3, None)

    def test_str_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, "invalid")

    def test_float_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 3, 5.5)

    def test_complex_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 3, complex(5))

    def test_dict_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, {"a": 1, "b": 2})

    def test_list_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, [1, 2, 3])

    def test_set_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, {1, 2, 3})

    def test_tuple_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, (1, 2, 3))

    def test_frozenset_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 3, frozenset({1, 2, 3, 1}))

    def test_range_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 3, range(5))

    def test_bytes_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 3, b'Python')

    def test_bytearray_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 3, bytearray(b'abcdefg'))

    def test_memoryview_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 3, memoryview(b'abcedfg'))

    def test_inf_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, float('inf'))

    def test_nan_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, float('nan'))

    def test_negative_y(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(3, 0, -1)


class TestSquare_order_of_initialization(unittest.TestCase):
    """Below are a unittests for testing order of Square attribute initialization."""

    def test_size_before_x(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("invalid size", "invalid x")

    def test_size_before_y(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("invalid size", 1, "invalid y")

    def test_x_before_y(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, "invalid x", "invalid y")


class TestSquare_area(unittest.TestCase):
    """Below are a unittests for testing the area method of the Square class."""

    def test_area_small(self):
        self.assertEqual(100, Square(10, 0, 0, 1).area())

    def test_area_large(self):
        y = Square(999999999999999999, 0, 0, 1)
        self.assertEqual(999999999999999998000000000000000001, y.area())

    def test_area_changed_attributes(self):
        y = Square(2, 0, 0, 1)
        y.size = 7
        self.assertEqual(49, y.area())

    def test_area_one_arg(self):
        y = Square(2, 10, 1, 1)
        with self.assertRaises(TypeError):
            y.area(1)


class TestSquare_stdout(unittest.TestCase):
    """Below are a unittests for testing __str__ and display methods of Square class."""

    @staticmethod
    def capture_stdout(sq, method):
        """It captures and returns text printed to stdout.
        Args:
            sq (Square): Square to print to stdout.
            method (str): Method to run on sq.
        Returns:
            The text printed to stdout by calling method on sq.
        """
        capture = io.StringIO()
        sys.stdout = capture
        if method == "print":
            print(sq)
        else:
            sq.display()
        sys.stdout = sys.__stdout__
        return capture

    def test_str_method_print_size(self):
        y = Square(4)
        capture = TestSquare_stdout.capture_stdout(y, "print")
        correct = "[Square] ({}) 0/0 - 4\n".format(y.id)
        self.assertEqual(correct, capture.getvalue())

    def test_str_method_size_x(self):
        y = Square(5, 5)
        correct = "[Square] ({}) 5/0 - 5".format(y.id)
        self.assertEqual(correct, y.__str__())

    def test_str_method_size_x_y(self):
        y = Square(7, 4, 22)
        correct = "[Square] ({}) 4/22 - 7".format(y.id)
        self.assertEqual(correct, str(y))

    def test_str_method_size_x_y_id(self):
        y = Square(2, 88, 4, 19)
        self.assertEqual("[Square] (19) 88/4 - 2", str(y))

    def test_str_method_changed_attributes(self):
        y = Square(7, 0, 0, [4])
        y.size = 15
        y.x = 8
        y.y = 10
        self.assertEqual("[Square] ([4]) 8/10 - 15", str(y))

    def test_str_method_one_arg(self):
        y = Square(1, 2, 3, 4)
        with self.assertRaises(TypeError):
            y.__str__(1)

    # Test display method
    def test_display_size(self):
        y = Square(2, 0, 0, 9)
        capture = TestSquare_stdout.capture_stdout(y, "display")
        self.assertEqual("##\n##\n", capture.getvalue())

    def test_display_size_x(self):
        y = Square(3, 1, 0, 18)
        capture = TestSquare_stdout.capture_stdout(y, "display")
        self.assertEqual(" ###\n ###\n ###\n", capture.getvalue())

    def test_display_size_y(self):
        y = Square(4, 0, 1, 9)
        capture = TestSquare_stdout.capture_stdout(y, "display")
        display = "\n####\n####\n####\n####\n"
        self.assertEqual(display, capture.getvalue())

    def test_display_size_x_y(self):
        y = Square(2, 3, 2, 1)
        capture = TestSquare_stdout.capture_stdout(y, "display")
        display = "\n\n   ##\n   ##\n"
        self.assertEqual(display, capture.getvalue())

    def test_display_one_arg(self):
        y = Square(3, 4, 5, 2)
        with self.assertRaises(TypeError):
            y.display(1)


class TestSquare_update_args(unittest.TestCase):
    """Below are a unittests for testing update args method of the Square class."""

    def test_update_args_zero(self):
        y = Square(10, 10, 10, 10)
        y.update()
        self.assertEqual("[Square] (10) 10/10 - 10", str(y))

    def test_update_args_one(self):
        y = Square(10, 10, 10, 10)
        y.update(89)
        self.assertEqual("[Square] (89) 10/10 - 10", str(y))

    def test_update_args_two(self):
        y = Square(10, 10, 10, 10)
        y.update(89, 2)
        self.assertEqual("[Square] (89) 10/10 - 2", str(y))

    def test_update_args_three(self):
        y = Square(10, 10, 10, 10)
        y.update(89, 2, 3)
        self.assertEqual("[Square] (89) 3/10 - 2", str(y))

    def test_update_args_four(self):
        y = Square(10, 10, 10, 10)
        y.update(89, 2, 3, 4)
        self.assertEqual("[Square] (89) 3/4 - 2", str(y))

    def test_update_args_more_than_four(self):
        y = Square(10, 10, 10, 10)
        y.update(89, 2, 3, 4, 5)
        self.assertEqual("[Square] (89) 3/4 - 2", str(y))

    def test_update_args_width_setter(self):
        y = Square(10, 10, 10, 10)
        y.update(89, 2)
        self.assertEqual(2, y.width)

    def test_update_args_height_setter(self):
        y = Square(10, 10, 10, 10)
        y.update(89, 2)
        self.assertEqual(2, y.height)

    def test_update_args_None_id(self):
        y = Square(10, 10, 10, 10)
        y.update(None)
        correct = "[Square] ({}) 10/10 - 10".format(y.id)
        self.assertEqual(correct, str(y))

    def test_update_args_None_id_and_more(self):
        y = Square(10, 10, 10, 10)
        y.update(None, 4, 5)
        correct = "[Square] ({}) 5/10 - 4".format(y.id)
        self.assertEqual(correct, str(y))

    def test_update_args_twice(self):
        y = Square(10, 10, 10, 10)
        y.update(89, 2, 3, 4)
        y.update(4, 3, 2, 89)
        self.assertEqual("[Square] (4) 2/89 - 3", str(y))

    def test_update_args_invalid_size_type(self):
        y = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            y.update(89, "invalid")

    def test_update_args_size_zero(self):
        y = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            y.update(89, 0)

    def test_update_args_size_negative(self):
        y = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            y.update(89, -4)

    def test_update_args_invalid_x(self):
        y = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            y.update(89, 1, "invalid")

    def test_update_args_x_negative(self):
        y = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            y.update(98, 1, -4)

    def test_update_args_invalid_y(self):
        y = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            y.update(89, 1, 2, "invalid")

    def test_update_args_y_negative(self):
        y = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            y.update(98, 1, 2, -4)

    def test_update_args_size_before_x(self):
        y = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            y.update(89, "invalid", "invalid")

    def test_update_args_size_before_y(self):
        y = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            y.update(89, "invalid", 2, "invalid")

    def test_update_args_x_before_y(self):
        y = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            y.update(89, 1, "invalid", "invalid")


class TestSquare_update_kwargs(unittest.TestCase):
    """Below are a unittests for testing update kwargs method of Square class."""

    def test_update_kwargs_one(self):
        y = Square(10, 10, 10, 10)
        y.update(id=1)
        self.assertEqual("[Square] (1) 10/10 - 10", str(y))

    def test_update_kwargs_two(self):
        y = Square(10, 10, 10, 10)
        y.update(size=1, id=2)
        self.assertEqual("[Square] (2) 10/10 - 1", str(y))

    def test_update_kwargs_three(self):
        y = Square(10, 10, 10, 10)
        y.update(y=1, size=3, id=89)
        self.assertEqual("[Square] (89) 10/1 - 3", str(y))

    def test_update_kwargs_four(self):
        y = Square(10, 10, 10, 10)
        y.update(id=89, x=1, y=3, size=4)
        self.assertEqual("[Square] (89) 1/3 - 4", str(y))

    def test_update_kwargs_width_setter(self):
        y = Square(10, 10, 10, 10)
        y.update(id=89, size=8)
        self.assertEqual(8, y.width)

    def test_update_kwargs_height_setter(self):
        y = Square(10, 10, 10, 10)
        y.update(id=89, size=9)
        self.assertEqual(9, y.height)

    def test_update_kwargs_None_id(self):
        y = Square(10, 10, 10, 10)
        y.update(id=None)
        correct = "[Square] ({}) 10/10 - 10".format(y.id)
        self.assertEqual(correct, str(y))

    def test_update_kwargs_None_id_and_more(self):
        y = Square(10, 10, 10, 10)
        y.update(id=None, size=7, x=18)
        correct = "[Square] ({}) 18/10 - 7".format(y.id)
        self.assertEqual(correct, str(y))

    def test_update_kwargs_twice(self):
        y = Square(10, 10, 10, 10)
        y.update(id=89, x=1)
        y.update(y=3, x=15, size=2)
        self.assertEqual("[Square] (89) 15/3 - 2", str(y))

    def test_update_kwargs_invalid_size(self):
        y = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            y.update(size="invalid")

    def test_update_kwargs_size_zero(self):
        y = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            y.update(size=0)

    def test_update_kwargs_size_negative(self):
        y = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            y.update(size=-3)

    def test_update_kwargs_invalid_x(self):
        y = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            y.update(x="invalid")

    def test_update_kwargs_x_negative(self):
        y = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            y.update(x=-5)

    def test_update_kwargs_invalid_y(self):
        y = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            y.update(y="invalid")

    def test_update_kwargs_y_negative(self):
        y = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            y.update(y=-5)

    def test_update_args_and_kwargs(self):
        y = Square(10, 10, 10, 10)
        y.update(89, 2, y=6)
        self.assertEqual("[Square] (89) 10/10 - 2", str(y))

    def test_update_kwargs_wrong_keys(self):
        y = Square(10, 10, 10, 10)
        y.update(a=5, b=10)
        self.assertEqual("[Square] (10) 10/10 - 10", str(y))

    def test_update_kwargs_some_wrong_keys(self):
        y = Square(10, 10, 10, 10)
        y.update(size=5, id=89, a=1, b=54)
        self.assertEqual("[Square] (89) 10/10 - 5", str(y))


class TestSquare_to_dictionary(unittest.TestCase):
    """Below are a unittests for testing to_dictionary method of the Square class."""

    def test_to_dictionary_output(self):
        y = Square(10, 2, 1, 1)
        correct = {'id': 1, 'x': 2, 'size': 10, 'y': 1}
        self.assertDictEqual(correct, y.to_dictionary())

    def test_to_dictionary_no_object_changes(self):
        y1 = Square(10, 2, 1, 2)
        y2 = Square(1, 2, 10)
        y2.update(**y1.to_dictionary())
        self.assertNotEqual(y1, y2)

    def test_to_dictionary_arg(self):
        y = Square(10, 10, 10, 10)
        with self.assertRaises(TypeError):
            y.to_dictionary(1)

if __name__ == "__main__":
    unittest.main()
