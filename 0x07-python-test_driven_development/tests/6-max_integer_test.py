import unittest
from max_integer import max_integer

class MaxIntegerTestCase(unittest.TestCase):
    def test_empty_list(self):
        result = max_integer([])
        self.assertIsNone(result)

    def test_positive_numbers(self):
        result = max_integer([1, 2, 3, 4, 5])
        self.assertEqual(result, 5)

    def test_negative_numbers(self):
        result = max_integer([-5, -4, -3, -2, -1])
        self.assertEqual(result, -1)

    def test_mixed_numbers(self):
        result = max_integer([-5, 10, 0, -2, 7])
        self.assertEqual(result, 10)

    def test_duplicate_numbers(self):
        result = max_integer([1, 2, 2, 2, 1])
        self.assertEqual(result, 2)

    def test_single_element_list(self):
        result = max_integer([7])
        self.assertEqual(result, 7)

    def test_large_numbers(self):
        result = max_integer([1000000, 999999, 10000000, 500000])
        self.assertEqual(result, 10000000)

    def test_float_numbers(self):
        result = max_integer([1.5, 2.7, 3.9, 2.2])
        self.assertEqual(result, 3.9)

if __name__ == '__main__':
    unittest.main()

