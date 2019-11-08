import unittest
from AlphaAffixedNumericType import AlphaAffixedNumericType


class TestAlphaAffixedNumericType(unittest.TestCase):

    def test_add_0_equal(self):
        v1 = AlphaAffixedNumericType('A123')
        expected = AlphaAffixedNumericType('A123').get_value()
        actual = (v1 + 0).get_value()
        self.assertEqual(actual, expected, f'actual: {actual}, expected: {expected}')

    def test_add_1_equal(self):
        v1 = AlphaAffixedNumericType('A123')
        expected = AlphaAffixedNumericType('A124').get_value()
        actual = (v1 + 1).get_value()
        self.assertEqual(actual, expected, f'actual: {actual}, expected: {expected}')

    def test_add_1000_equal(self):
        v1 = AlphaAffixedNumericType('A123')
        expected = AlphaAffixedNumericType('A1123').get_value()
        actual = (v1 + 1000).get_value()
        self.assertEqual(actual, expected, f'actual: {actual}, expected: {expected}')

    def test_minus_1_equal(self):
        v1 = AlphaAffixedNumericType('A123')
        expected = AlphaAffixedNumericType('A122').get_value()
        actual = (v1 - 1 ).get_value()
        self.assertEqual(actual, expected, f'actual: {actual}, expected: {expected}')

    def test_minus_self_is_0(self):
        v1 = AlphaAffixedNumericType('A123')
        expected = 0
        actual = v1 - v1
        self.assertEqual(actual, expected, f'actual: {actual}, expected: {expected}')

    def test_minus_1_less_than_self_is_1(self):
        v1 = AlphaAffixedNumericType('A123')
        expected = 1
        actual = v1 - AlphaAffixedNumericType('A122')
        self.assertEqual(actual, expected, f'actual: {actual}, expected: {expected}')

if __name__ == '__main__':
    unittest.main()