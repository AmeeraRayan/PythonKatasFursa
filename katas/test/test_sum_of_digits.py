import unittest
from katas.sum_of_digits import sum_of_digits

class TestSumOfDigits(unittest.TestCase):
    def test_basic_numbers(self):
        self.assertEqual(sum_of_digits("abc123"), 6)  # 1 + 2 + 3 = 6

    def test_numbers_with_words(self):
        self.assertEqual(sum_of_digits("5 cats and 2 dogs"), 7)  # 5 + 2 = 7

    def test_no_numbers(self):
        self.assertEqual(sum_of_digits("No digits here!"), 0)  # No digits → 0

    def test_only_numbers(self):
        self.assertEqual(sum_of_digits("1234567890"), 45)  # 1+2+3+...+9+0 = 45

    def test_empty_string(self):
        self.assertEqual(sum_of_digits(""), 0)  # Nothing → 0

    def test_spaces_and_numbers(self):
        self.assertEqual(sum_of_digits("  9 8 7 "), 24)  # 9+8+7 = 24

    def test_special_characters(self):
        self.assertEqual(sum_of_digits("!@#4$%^5&*()6"), 15)  # 4+5+6 = 15

    def test_large_numbers_but_single_digits(self):
        self.assertEqual(sum_of_digits("123abc456def789"), 45)  # 1+2+3+4+5+6+7+8+9 = 45

    def test_leading_zeros(self):
        self.assertEqual(sum_of_digits("000123"), 6)  # 0+0+0+1+2+3 = 6

    def test_uppercase_letters(self):
        self.assertEqual(sum_of_digits("ABC1D2E3"), 6)  # 1+2+3 = 6
