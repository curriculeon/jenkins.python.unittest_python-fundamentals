# Created by Leon Hunter at 5:11 PM 10/24/2020
def nullary_function_assert_equals(self, method_to_be_tested, value_sets):
    for value_set in value_sets:
        # given
        expected_output = value_set[0]

        # when
        actual_output = method_to_be_tested()

        calculation_error_message = '''            
           expected_output = {}
           actual_output = {}
           '''.format(expected_output, actual_output)

        # then
        self.assertEquals(expected_output, actual_output, calculation_error_message)


def unary_function_assert_equals(self, method_to_be_tested, value_sets):
    for value_set in value_sets:
        # given
        first_value = value_set[0]
        expected_output = value_set[2]

        # when
        actual_output = method_to_be_tested(first_value)

        calculation_error_message = '''
           first_value = {}
           expected_output = {}
           actual_output = {}
           '''.format(first_value, expected_output, actual_output)

        # then
        self.assertEquals(expected_output, actual_output, calculation_error_message)


def binary_function_assert_equals(self, method_to_be_tested, value_sets):
    for value_set in value_sets:
        # given
        first_value = value_set[0]
        second_value = value_set[1]
        expected_output = value_set[2]

        # when
        actual_output = method_to_be_tested(first_value, second_value)

        calculation_error_message = '''
           first_value = {}
           second_value = {}            
           expected_output = {}
           actual_output = {}
           '''.format(first_value, second_value, expected_output, actual_output)

        # then
        self.assertEquals(expected_output, actual_output, calculation_error_message)


def ternary_function_assert_equals(self, method_to_be_tested, value_sets):
    for value_set in value_sets:
        # given
        first_value = value_set[0]
        second_value = value_set[1]
        third_value = value_set[2]
        expected_output = value_set[3]

        # when
        actual_output = method_to_be_tested(first_value, second_value, third_value)

        calculation_error_message = '''
           first_value = {}
           second_value = {}
           third_value = {}
           expected_output = {}
           actual_output = {}
           '''.format(first_value, second_value, third_value, expected_output, actual_output)

        # then
        self.assertEquals(expected_output, actual_output, calculation_error_message)