import unittest
from polynomials import*

class TestPolynomials(unittest.TestCase):
    def test_derivative_of_number(self):
        result='0'
        polynomial = Polynomial([Term('42')])
        self.assertEqual(polynomial.term_derivatives(),result)

    def test_derivative_of_linear_function(self):
        result = '7'
        polynomial = Polynomial([Term('7x')])
        self.assertEqual(polynomial.term_derivatives(),result)

    def test_derivative_of_quadratic_function_with_a0(self):
        result = '16x + 4'
        polynomial = Polynomial([Term('8x^2'),Term('4x'),Term('17')])
        self.assertEqual(polynomial.term_derivatives(),result)

    def test_derivative_of_different_degree_terms(self):
        result = '1330x^6 + 220x^3 + 8x'
        polynomial = Polynomial([Term('190x^7'),Term('55x^4'),Term('4x^2')])
        self.assertEqual(polynomial.term_derivatives(),result)

    def test_when_derivative_of_duplicate_term_degrees_greater_than_one(self):
        result = '75x^2 + 46x'
        polynomial= Polynomial([Term('21x^2'),Term('25x^3'),Term('2x^2')])
        self.assertEqual(polynomial.term_derivatives(),result)

    def test_when_derivative_of_duplicate_degrees_including_first(self):
        result = '75x^2 + 46x + 39'
        polynomial= Polynomial([Term('25x'),Term('21x^2'),Term('25x^3'),Term('14x'),Term('2x^2')])
        self.assertEqual(polynomial.term_derivatives(),result)

    def test_when_derivative_of_all_term_degrees(self):
        result = '595x^6 + 159x^2 + 28x + 12'
        polynomial = Polynomial([Term('11'),Term('41x^3'),Term('12x^3'),Term('14x^2'),Term('3x'),Term('1'),Term('9x'),Term('85x^7')])
        self.assertEqual(polynomial.term_derivatives(),result)


if __name__=='__main__':
    unittest.main()
