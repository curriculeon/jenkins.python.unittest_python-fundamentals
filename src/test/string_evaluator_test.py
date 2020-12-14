# Created by Leon Hunter at 3:57 PM 10/23/2020
from unittest import TestCase

from src.main.string_evaluator import StringManipulator
from src.test import testutils


class StringManipulatorTest(TestCase):
    def test_substring_inclusive(self):
        testutils.ternary_function_assert_equals(StringManipulator().substring_inclusive, [
            ("Hello", 0, 4, "Hello"),
            ("Hello", 0, 3, "Hell"),
            ("Hello", 1, 4, "ello"),
        ])

    def test_substring_exclusive(self):
        testutils.ternary_function_assert_equals(StringManipulator().substring_exclusive, [
            ("Hello", 0, 4, "ell"),
            ("Hello", 0, 3, "el"),
            ("Hello", 1, 4, "ll")
        ])

    def test_concatenate(self):
        testutils.binary_function_assert_equals(StringManipulator().concatenate, [
            ("Hello", "World", "HelloWorld"),
            (19, 93, "1993"),
            (19, "", "19"),
            (None, "None", "NoneNone")
        ])

    def test_compare(self):
        testutils.binary_function_assert_equals(StringManipulator().compare, [
            ("Hello", 0, False),
            ("Hello", "Hello", True),
            ("0", 0, True),
            (None, 0, True),
            (False, 0, True),
            (True, 1, True)
        ])

    def test_get_first_word(self):
        testutils.unary_function_assert_equals(StringManipulator().get_first_word, [
            ("The quick brown fox", "The"),
            ("Quick Brown Fox", "Quick"),
            ("Brown Fox", "Brown"),
        ])

    def test_get_second_word(self):
        testutils.unary_function_assert_equals(StringManipulator().get_second_word, [
            ("The quick brown fox", "quick"),
            ("Quick Brown Fox", "Brown"),
            ("Brown Fox", "Fox"),
        ])

    def test_get_hello_world(self):
        testutils.nullary_function_assert_equals(StringManipulator().get_hello_world, [["Hello World"]])
