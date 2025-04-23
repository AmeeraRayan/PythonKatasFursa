import unittest
from katas.reduce_list import reduce_array

class TestReduceArray(unittest.TestCase):
    def test_basic_case(self):
        nums = [10, 15, 7, 20, 25]
        reduce_array(nums)
        self.assertEqual(nums, [10, 5, -8, 13, 5])

    def test_single_element(self):
        nums = [5]
        reduce_array(nums)
        self.assertEqual(nums, [5])  # No change for one element

    def test_empty_list(self):
        nums = []
        reduce_array(nums)
        self.assertEqual(nums, [])  # Still empty

    def test_all_same_numbers(self):
        nums = [4, 4, 4, 4]
        reduce_array(nums)
        self.assertEqual(nums, [4, 0, 0, 0])

    def test_negative_numbers(self):
        nums = [-10, -5, -15, 0]
        reduce_array(nums)
        self.assertEqual(nums, [-10, 5, -10, 15])
