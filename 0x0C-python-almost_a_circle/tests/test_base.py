#!/usr/bin/python3

"""Which defines unittests for base.py.
Unittest classes:
    TestBase_instantiation - line 23
    TestBase_to_json_string - line 110
    TestBase_save_to_file - line 156
    TestBase_from_json_string - line 234
    TestBase_create - line 288
    TestBase_load_from_file - line 340
    TestBase_save_to_file_csv - line 406
    TestBase_load_from_file_csv - line 484
"""
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import os
import unittest


class TestBase_instantiation(unittest.TestCase):
    """Below are a unittests for testing instantiation of the Base class."""

    def test_three_bases(self):
        """Below are a unittests for testing test_three_bases"""

        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 2)

    def test_no_arg(self):
        """Below are a unittests for testing test_no_arg(self)"""

        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_unique_id(self):
        """Below are a unittests for test_unique_id"""

        self.assertEqual(12, Base(12).id)

    def test_None_id(self):
        """Below are a unittests for test_None_id"""

        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, b2.id - 1)

    def test_id_public(self):
        """Below are a unittests for test_id_public"""

        b = Base(12)
        b.id = 15
        self.assertEqual(15, b.id)

    def test_nb_instances_after_unique_id(self):
        """Below are a unittests for
        test_nb_instances_after_unique_id"""

        b1 = Base()
        b2 = Base(12)
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 1)

    def test_nb_instances_private(self):
        """Below are a unittests for
        test_nb_instances_private"""

        with self.assertRaises(AttributeError):
            print(Base(12).__nb_instances)

    def test_str_id(self):
        """Below are a unittests for test_str_id"""

        self.assertEqual("hello", Base("hello").id)

    def test_float_id(self):
        """Below are a unittests for test_float_id"""

        self.assertEqual(5.5, Base(5.5).id)

    def test_dict_id(self):
        """Below are a unittests for test_dict_id"""

        self.assertEqual({"a": 1, "b": 2}, Base({"a": 1, "b": 2}).id)

    def test_complex_id(self):
        """Below are a unittests for test_complex_id"""

        self.assertEqual(complex(5), Base(complex(5)).id)

    def test_bool_id(self):
        """Below are a unittests for test_bool_id"""

        self.assertEqual(True, Base(True).id)

    def test_list_id(self):
        """Below are a unittests for test_list_id"""

        self.assertEqual([1, 2, 3], Base([1, 2, 3]).id)

    def test_tuple_id(self):
        """Below are a unittests for test_tuple_id"""

        self.assertEqual((1, 2), Base((1, 2)).id)

    def test_set_id(self):
        """Below are a unittests for test_set_id"""

        self.assertEqual({1, 2, 3}, Base({1, 2, 3}).id)

    def test_frozenset_id(self):
        """Below are a unittests for test_frozenset_id"""

        self.assertEqual(frozenset({1, 2, 3}),
                         Base(frozenset({1, 2, 3})).id)

    def test_range_id(self):
        """Below are a unittests for test_range_id"""

        self.assertEqual(range(5), Base(range(5)).id)

    def test_bytes_id(self):
        """Below are a unittests for test_bytes_id"""

        self.assertEqual(b'Python', Base(b'Python').id)

    def test_memoryview_id(self):
        """Below are a unittests for test_memoryview_id"""

        self.assertEqual(memoryview(b'abcefg'), Base(memoryview(b'abcefg')).id)

    def test_inf_id(self):
        """Below are a unittests for test_inf_id"""

        self.assertEqual(float('inf'), Base(float('inf')).id)

    def test_bytearray_id(self):
        """Below are a unittests for test_bytearray_id"""

        self.assertEqual(bytearray(b'abcefg'), Base(bytearray(b'abcefg')).id)

    def test_NaN_id(self):
        """Below are a unittests for test_NaN_id"""

        self.assertNotEqual(float('nan'), Base(float('nan')).id)

    def test_two_args(self):
        with self.assertRaises(TypeError):
            Base(1, 2)


class TestBase_to_json_string(unittest.TestCase):
    """ for testing Below are a unittests
     to_json_string method of Base class."""

    def test_to_json_string_rectangle_type(self):
        x = Rectangle(10, 7, 2, 8, 6)
        self.assertEqual(str, type(Base.to_json_string([x.to_dictionary()])))

    def test_to_json_string_rectangle_two_dicts(self):
        x1 = Rectangle(2, 3, 5, 19, 2)
        x2 = Rectangle(4, 2, 4, 1, 12)
        list_dicts = [x1.to_dictionary(), x2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(list_dicts)) == 106)

    def test_to_json_string_rectangle_one_dict(self):
        x = Rectangle(10, 7, 2, 8, 6)
        self.assertTrue(len(Base.to_json_string([x.to_dictionary()])) == 53)

    def test_to_json_string_square_one_dict(self):
        y = Square(10, 2, 3, 4)
        self.assertTrue(len(Base.to_json_string([y.to_dictionary()])) == 39)

    def test_to_json_string_square_type(self):
        y = Square(10, 2, 3, 4)
        self.assertEqual(str, type(Base.to_json_string([y.to_dictionary()])))

    def test_to_json_string_square_two_dicts(self):
        y1 = Square(10, 2, 3, 4)
        y2 = Square(4, 5, 21, 2)
        list_dicts = [y1.to_dictionary(), y2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(list_dicts)) == 78)

    def test_to_json_string_none(self):
        self.assertEqual("[]", Base.to_json_string(None))

    def test_to_json_string_empty_list(self):
        self.assertEqual("[]", Base.to_json_string([]))

    def test_to_json_string_no_args(self):
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_to_json_string_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.to_json_string([], 1)


class TestBase_save_to_file(unittest.TestCase):
    """Below are a unittests for
    testing save_to_file method of Base class."""

    @classmethod
    def tearDown(self):
        """Which deletes any created files."""
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass
        try:
            os.remove("Base.json")
        except IOError:
            pass

    def test_save_to_file_one_rectangle(self):
        x = Rectangle(10, 7, 2, 8, 5)
        Rectangle.save_to_file([x])
        with open("Rectangle.json", "x") as f:
            self.assertTrue(len(f.read()) == 53)

    def test_save_to_file_one_square(self):
        y = Square(10, 7, 2, 8)
        Square.save_to_file([y])
        with open("Square.json", "x") as f:
            self.assertTrue(len(f.read()) == 39)

    def test_save_to_file_two_rectangles(self):
        x1 = Rectangle(10, 7, 2, 8, 5)
        x2 = Rectangle(2, 4, 1, 2, 3)
        Rectangle.save_to_file([x1, x2])
        with open("Rectangle.json", "x") as f:
            self.assertTrue(len(f.read()) == 105)

    def test_save_to_file_two_squares(self):
        y1 = Square(10, 7, 2, 8)
        y2 = Square(8, 1, 2, 3)
        Square.save_to_file([y1, y2])
        with open("Square.json", "x") as f:
            self.assertTrue(len(f.read()) == 77)

    def test_save_to_file_cls_name_for_filename(self):
        y = Square(10, 7, 2, 8)
        Base.save_to_file([y])
        with open("Base.json", "x") as f:
            self.assertTrue(len(f.read()) == 39)

    def test_save_to_file_overwrite(self):
        y = Square(9, 2, 39, 2)
        Square.save_to_file([y])
        y = Square(10, 7, 2, 8)
        Square.save_to_file([y])
        with open("Square.json", "x") as f:
            self.assertTrue(len(f.read()) == 39)

    def test_save_to_file_None(self):
        Square.save_to_file(None)
        with open("Square.json", "x") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_empty_list(self):
        Square.save_to_file([])
        with open("Square.json", "x") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file()

    def test_save_to_file_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Square.save_to_file([], 1)


class TestBase_from_json_string(unittest.TestCase):
    """Below are a unittests for testing
    from_json_string method of Base class."""

    def test_from_json_string_type(self):
        list_input = [{"id": 89, "width": 10, "height": 4}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list, type(list_output))

    def test_from_json_string_one_rectangle(self):
        list_input = [{"id": 89, "width": 10, "height": 4, "x": 7}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_two_rectangles(self):
        list_input = [
            {"id": 89, "width": 10, "height": 4, "x": 7, "y": 8},
            {"id": 98, "width": 5, "height": 2, "x": 1, "y": 3},
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_one_square(self):
        list_input = [{"id": 89, "size": 10, "height": 4}]
        json_list_input = Square.to_json_string(list_input)
        list_output = Square.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_two_squares(self):
        list_input = [
            {"id": 89, "size": 10, "height": 4},
            {"id": 7, "size": 1, "height": 7}
        ]
        json_list_input = Square.to_json_string(list_input)
        list_output = Square.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_None(self):
        self.assertEqual([], Base.from_json_string(None))

    def test_from_json_string_empty_list(self):
        self.assertEqual([], Base.from_json_string("[]"))

    def test_from_json_string_no_args(self):
        with self.assertRaises(TypeError):
            Base.from_json_string()

    def test_from_json_string_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.from_json_string([], 1)


class TestBase_create(unittest.TestCase):
    """Below are a unittests for testing create method of Base class."""

    def test_create_rectangle_original(self):
        x1 = Rectangle(3, 5, 1, 2, 7)
        x1_dictionary = x1.to_dictionary()
        x2 = Rectangle.create(**x1_dictionary)
        self.assertEqual("[Rectangle] (7) 1/2 - 3/5", str(x1))

    def test_create_rectangle_new(self):
        x1 = Rectangle(3, 5, 1, 2, 7)
        x1_dictionary = x1.to_dictionary()
        x2 = Rectangle.create(**x1_dictionary)
        self.assertEqual("[Rectangle] (7) 1/2 - 3/5", str(x2))

    def test_create_rectangle_is(self):
        x1 = Rectangle(3, 5, 1, 2, 7)
        x1_dictionary = x1.to_dictionary()
        x2 = Rectangle.create(**x1_dictionary)
        self.assertIsNot(x1, x2)

    def test_create_rectangle_equals(self):
        x1 = Rectangle(3, 5, 1, 2, 7)
        x1_dictionary = x1.to_dictionary()
        x2 = Rectangle.create(**x1_dictionary)
        self.assertNotEqual(x1, x2)

    def test_create_square_original(self):
        y1 = Square(3, 5, 1, 7)
        y1_dictionary = y1.to_dictionary()
        y2 = Square.create(**y1_dictionary)
        self.assertEqual("[Square] (7) 5/1 - 3", str(y1))

    def test_create_square_new(self):
        y1 = Square(3, 5, 1, 7)
        y1_dictionary = y1.to_dictionary()
        y2 = Square.create(**y1_dictionary)
        self.assertEqual("[Square] (7) 5/1 - 3", str(y2))

    def test_create_square_is(self):
        y1 = Square(3, 5, 1, 7)
        y1_dictionary = y1.to_dictionary()
        y2 = Square.create(**y1_dictionary)
        self.assertIsNot(y1, y2)

    def test_create_square_equals(self):
        y1 = Square(3, 5, 1, 7)
        y1_dictionary = y1.to_dictionary()
        y2 = Square.create(**y1_dictionary)
        self.assertNotEqual(y1, y2)


class TestBase_load_from_file(unittest.TestCase):
    """Below are a unittests
    for testing load_from_file_method of Base class."""

    @classmethod
    def tearDown(self):
        """Which deletes any created files."""
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass

    def test_load_from_file_first_rectangle(self):
        x1 = Rectangle(10, 7, 2, 8, 1)
        x2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file([x1, x2])
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(str(x1), str(list_rectangles_output[0]))

    def test_load_from_file_second_rectangle(self):
        x1 = Rectangle(10, 7, 2, 8, 1)
        x2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file([x1, x2])
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(str(x2), str(list_rectangles_output[1]))

    def test_load_from_file_rectangle_types(self):
        x1 = Rectangle(10, 7, 2, 8, 1)
        x2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file([x1, x2])
        output = Rectangle.load_from_file()
        self.assertTrue(
            all(type(obj) is Rectangle for obj in output))

    def test_load_from_file_first_square(self):
        y1 = Square(5, 1, 3, 3)
        y2 = Square(9, 5, 2, 3)
        Square.save_to_file([y1, y2])
        list_squares_output = Square.load_from_file()
        self.assertEqual(str(y1), str(list_squares_output[0]))

    def test_load_from_file_second_square(self):
        y1 = Square(5, 1, 3, 3)
        y2 = Square(9, 5, 2, 3)
        Square.save_to_file([y1, y2])
        list_squares_output = Square.load_from_file()
        self.assertEqual(str(y2), str(list_squares_output[1]))

    def test_load_from_file_square_types(self):
        y1 = Square(5, 1, 3, 3)
        y2 = Square(9, 5, 2, 3)
        Square.save_to_file([y1, y2])
        output = Square.load_from_file()
        self.assertTrue(all(type(obj) is Square for obj in output))

    def test_load_from_file_no_file(self):
        output = Square.load_from_file()
        self.assertEqual([], output)

    def test_load_from_file_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.load_from_file([], 1)


class TestBase_save_to_file_csv(unittest.TestCase):
    """Below are a unittests for testing
    save_to_file_csv method of Base class."""

    @classmethod
    def tearDown(self):
        """Which deletes any created files."""
        try:
            os.remove("Rectangle.csv")
        except IOError:
            pass
        try:
            os.remove("Square.csv")
        except IOError:
            pass
        try:
            os.remove("Base.csv")
        except IOError:
            pass

    def test_save_to_file_csv_one_rectangle(self):
        x = Rectangle(10, 7, 2, 8, 5)
        Rectangle.save_to_file_csv([x])
        with open("Rectangle.csv", "x") as f:
            self.assertTrue("5,10,7,2,8", f.read())

    def test_save_to_file_csv_two_rectangles(self):
        x1 = Rectangle(10, 7, 2, 8, 5)
        x2 = Rectangle(2, 4, 1, 2, 3)
        Rectangle.save_to_file_csv([x1, x2])
        with open("Rectangle.csv", "x") as f:
            self.assertTrue("5,10,7,2,8\n2,4,1,2,3", f.read())

    def test_save_to_file_csv_one_square(self):
        y = Square(10, 7, 2, 8)
        Square.save_to_file_csv([y])
        with open("Square.csv", "x") as f:
            self.assertTrue("8,10,7,2", f.read())

    def test_save_to_file_csv_two_squares(self):
        y1 = Square(10, 7, 2, 8)
        y2 = Square(8, 1, 2, 3)
        Square.save_to_file_csv([y1, y2])
        with open("Square.csv", "x") as f:
            self.assertTrue("8,10,7,2\n3,8,1,2", f.read())

    def test_save_to_file__csv_cls_name(self):
        y = Square(10, 7, 2, 8)
        Base.save_to_file_csv([y])
        with open("Base.csv", "x") as f:
            self.assertTrue("8,10,7,2", f.read())

    def test_save_to_file_csv_overwrite(self):
        y = Square(9, 2, 39, 2)
        Square.save_to_file_csv([y])
        y = Square(10, 7, 2, 8)
        Square.save_to_file_csv([y])
        with open("Square.csv", "x") as f:
            self.assertTrue("8,10,7,2", f.read())

    def test_save_to_file__csv_None(self):
        Square.save_to_file_csv(None)
        with open("Square.csv", "x") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_csv_empty_list(self):
        Square.save_to_file_csv([])
        with open("Square.csv", "x") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_csv_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file_csv()

    def test_save_to_file_csv_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Square.save_to_file_csv([], 1)


class TestBase_load_from_file_csv(unittest.TestCase):
    """Below are a unittests for testing
    method of Base class."""

    @classmethod
    def tearDown(self):
        """Which deletes any created files."""
        try:
            os.remove("Rectangle.csv")
        except IOError:
            pass
        try:
            os.remove("Square.csv")
        except IOError:
            pass

    def test_load_from_file_csv_first_rectangle(self):
        x1 = Rectangle(10, 7, 2, 8, 1)
        x2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file_csv([x1, x2])
        list_rectangles_output = Rectangle.load_from_file_csv()
        self.assertEqual(str(x1), str(list_rectangles_output[0]))

    def test_load_from_file_csv_second_rectangle(self):
        x1 = Rectangle(10, 7, 2, 8, 1)
        x2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file_csv([x1, x2])
        list_rectangles_output = Rectangle.load_from_file_csv()
        self.assertEqual(str(x2), str(list_rectangles_output[1]))

    def test_load_from_file_csv_rectangle_types(self):
        x1 = Rectangle(10, 7, 2, 8, 1)
        x2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file_csv([x1, x2])
        output = Rectangle.load_from_file_csv()
        self.assertTrue(all(type(obj) is Rectangle for obj in output))

    def test_load_from_file_csv_first_square(self):
        y1 = Square(5, 1, 3, 3)
        y2 = Square(9, 5, 2, 3)
        Square.save_to_file_csv([y1, y2])
        list_squares_output = Square.load_from_file_csv()
        self.assertEqual(str(y1), str(list_squares_output[0]))

    def test_load_from_file_csv_second_square(self):
        y1 = Square(5, 1, 3, 3)
        y2 = Square(9, 5, 2, 3)
        Square.save_to_file_csv([y1, y2])
        list_squares_output = Square.load_from_file_csv()
        self.assertEqual(str(y2), str(list_squares_output[1]))

    def test_load_from_file_csv_square_types(self):
        y1 = Square(5, 1, 3, 3)
        y2 = Square(9, 5, 2, 3)
        Square.save_to_file_csv([y1, y2])
        output = Square.load_from_file_csv()
        self.assertTrue(all(type(obj) is Square for obj in output))

    def test_load_from_file_csv_no_file(self):
        output = Square.load_from_file_csv()
        self.assertEqual([], output)

    def test_load_from_file_csv_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.load_from_file_csv([], 1)


if __name__ == "__main__":
    unittest.main()
