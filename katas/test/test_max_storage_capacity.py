import unittest
from katas.max_storage_capacity import max_storage_area  # Adjust path if needed

class TestMaxStorageArea(unittest.TestCase):
    def test_example_case(self):
        self.assertEqual(max_storage_area([2, 1, 5, 6, 2, 3]), 10)

    def test_all_same_height(self):
        self.assertEqual(max_storage_area([3, 3, 3, 3]), 12)  # 3 × 4

    def test_increasing_heights(self):
        self.assertEqual(max_storage_area([1, 2, 3, 4, 5]), 9)  # 3 × 3

    def test_decreasing_heights(self):
        self.assertEqual(max_storage_area([5, 4, 3, 2, 1]), 9)  # 3 × 3

    def test_single_bar(self):
        self.assertEqual(max_storage_area([4]), 4)

    def test_empty(self):
        self.assertEqual(max_storage_area([]), 0)

    def test_with_zero_height(self):
        self.assertEqual(max_storage_area([2, 0, 2]), 2)  # best is just the first or last bar