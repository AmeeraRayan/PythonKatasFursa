import unittest
from katas.list_diff import find_difference

class TestFindDifference(unittest.TestCase):
    def test_normal_case(self):
        self.assertEqual(find_difference([10, 3, 5, 6, 20, -2]), 22)

    def test_all_positive(self):
        self.assertEqual(find_difference([1, 2, 3, 4, 5]), 4)

    def test_all_negative(self):
        self.assertEqual(find_difference([-10, -3, -5, -1]), 9)

    def test_same_numbers(self):
        self.assertEqual(find_difference([5, 5, 5]), 0)

    def test_two_numbers(self):
        self.assertEqual(find_difference([100, 50]), 50)
