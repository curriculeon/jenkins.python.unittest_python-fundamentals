# Created by Leon Hunter at 11:23 AM 10/24/2020
from unittest import TestCase

from src.main.predicator import Predicator


class PredicatorTester(TestCase):
    def _test(self, method_to_be_tested, value_sets):
        for value_set in value_sets:
            # given
            first_value = value_set[0]
            expected_calculation = value_set[1]

            # when
            actual_calculation = method_to_be_tested(first_value)

            calculation_error_message = '''
            first_value = {}
            expected_calculation = {}
            actual_calculation = {}
            '''.format(first_value, expected_calculation, actual_calculation)

            return_type_error_message = '''
            expected return value of `{}` to be of type `bool`
            instead was of type `{}`
            '''.format(method_to_be_tested.__name__, type(actual_calculation))

            # then
            self.assertTrue(isinstance(actual_calculation, bool), return_type_error_message)
            self.assertAlmostEqual(expected_calculation, actual_calculation, calculation_error_message)

    def test_is_greater_than_5(self):
        self._test(Predicator().is_greater_than_5, [
            (1, False),
            (5, False),
            (6, True),
            (7, True)
        ])

    def test_is_greater_than_8(self):
        self._test(Predicator().is_greater_than_8, [
            (1, False),
            (8, False),
            (10, True),
            (17, True)
        ])

    def test_is_less_than_1(self):
        self._test(Predicator().is_less_than_1, [
            (5, False),
            (1, False),
            (-6, True),
            (-7, True)
        ])

    def test_is_less_than_4(self):
        self._test(Predicator().is_less_than_4, [
            (5, False),
            (4, False),
            (2, True),
            (-7, True)
        ])
