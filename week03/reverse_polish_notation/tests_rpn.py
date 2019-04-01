import unittest
from rpn_calculate import rpn_calc

class TestReversePolishNotation(unittest.TestCase):
    def test_when_single_digit_is_passed_return_the_same_digit(self):
        expression = '188'
        expected_result = int(expression)
        self.assertEqual(rpn_calc(expression),expected_result)

    def test_when_two_numbers_are_passed_then_return_sum_of_them(self):
        expression ='4 8 +'
        expected_result=12
        self.assertEqual(rpn_calc(expression),expected_result)

    def test_when_substraction(self):
        expression = '3 5 6 - -'
        expected_result= 4
        self.assertEqual(rpn_calc(expression),expected_result)

    def test_when_sqrt(self):
        expression = '9 SQRT'
        expected_result = 3
        self.assertEqual(rpn_calc(expression),expected_result)

    def test_when_division(self):
        expression = '20 4 /'
        expected_result = 5
        self.assertEqual(rpn_calc(expression),expected_result)

    def test_when_combined_addition_and_substraction(self):
        expression = '4 2 + 3 -'
        expected_result = 3 
        self.assertEqual(rpn_calc(expression),expected_result)

    def test_when_combined_addition_and_multiplication(self):
        expression = '3 5 8 * 7 + *'
        expected_result = 141
        self.assertEqual(rpn_calc(expression),expected_result)

    def test_when_combined_some_operations(self):
        expression = '1 2 3 5 + + * 10 * SQRT'
        expected_result = 10
        self.assertEqual(rpn_calc(expression),expected_result)

    def test_when_floor_division(self):
        expression = '4 17 2 // +'
        expected_result = 12
        self.assertEqual(rpn_calc(expression),expected_result)

    def test_when_exponentiation(self):
        expression = '6 11 2 ** -'
        expected_result = -115
        self.assertEqual(rpn_calc(expression),expected_result)

    def test_when_abs(self):
        expression = '2 5 - ABS 4 1 + *'
        expected_result = 15
        self.assertEqual(rpn_calc(expression),expected_result)

    def test_when_max(self):
        expression = '2 5 + 4 8 + 5 MAX 3 *'
        expected_result = 36
        self.assertEqual(rpn_calc(expression),expected_result)

    def test_when_min(self):
        expression = '2 5 - ABS 4 8 - 5 MIN 3 * ABS'
        expected_result = 12
        self.assertEqual(rpn_calc(expression),expected_result)

    def test_when_all_operations(self):
        expression = '11 4 5 - * ABS 14 + SQRT 4 2 MAX 45 * SQRT 12 10 1 - MIN 3 // 77 + 4 **'
        expected_result = 40960000
        self.assertEqual(rpn_calc(expression),expected_result)


if __name__=='__main__':
    unittest.main()
