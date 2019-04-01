import unittest
from simplify_fraction import *
from collect_fractions import *
from sort_fractions import *

class TestingFractions(unittest.TestCase):
    def test_validate_fraction_object_is_tuple(self):
         with self.assertRaises(ValidationError) as exception:
             simplify_fraction([1,2])

    def test_when_equal_nominator_denominator(self):
        fraction = (2,2)
        expected_result = (1,1)
        self.assertEqual(simplify_fraction(fraction),expected_result)

    def test_when_nominator_bigger_than_denominator_and_division_remainder_equal_zero(self):
        fraction = (15,3)
        expected_result = (5,1)
        self.assertEqual(simplify_fraction(fraction),expected_result)

    def test_when_denominator_equal_zero(self):
        with self.assertRaises(ZeroDivisionError) as exception:
            simplify_fraction((90,0))

    def test_when_nominator_equal_zero(self):
        fraction = (0,22)
        expected_result = (0,22)
        self.assertEqual(simplify_fraction(fraction),expected_result)

    def test_when_simplified_fraction(self):
        fraction = (11,3)
        expected_result = (11,3)
        self.assertEqual(simplify_fraction(fraction),expected_result)

    def test_when_simplifying_fraction_where_nominator_bigger_than_denominator(self):
        fraction = (81,6)
        expected_result = (27,2)
        self.assertEqual(simplify_fraction(fraction),expected_result)

    def test_when_simplifying_fraction_where_denominator_bigger_than_nominator(self):
        fraction = (10,66)
        expected_result = (5,33)
        self.assertEqual(simplify_fraction(fraction),expected_result)

    def test_when_collecting_one_fraction(self):
        fractions = [(10,2)]
        expected_result = (5,1)
        self.assertEqual(collect_fractions(fractions),expected_result)

    def test_when_collecting_two_fractions(self):
        fractions = [(1, 7), (2, 6)]
        expected_result = (10,21)
        self.assertEqual(collect_fractions(fractions),expected_result)

    def test_when_collection_more_than_two_fractions(self):
        fractions = [(1, 2),(1,2),(1,3),(1,3),(5,3),(7,7)]
        expected_result = (13,3)
        self.assertEqual(collect_fractions(fractions),expected_result)

    def test_when_collection_contains_fraction_with_zero_denominator(self):
        with self.assertRaises(ZeroDivisionError) as exception:
            collect_fractions([(1, 2),(1,2),(1,3),(1,3),(5,3),(7,0)])

    def test_when_sorting_fractions_including_duplicate_fractions(self):
        fractions = [(1, 2), (1, 3), (1,8), (9,15), (1,2), (1,3), (1,2)]
        expected_result = [(1,8), (1,3), (1,3), (1,2), (1,2), (1,2), (9,15)]
        self.assertEqual(sort_fractions(fractions),expected_result)

    def test_when_sorting_fractions(self):
        fractions = [(5, 6), (22, 78), (22, 7), (7, 8), (9, 6), (15, 32)]
        expected_result = [(22, 78), (15, 32), (5, 6), (7, 8), (9, 6), (22, 7)]
        self.assertEqual(sort_fractions(fractions),expected_result)

if __name__ == '__main__':
    unittest.main()
