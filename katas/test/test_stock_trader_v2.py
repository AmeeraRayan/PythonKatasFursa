import unittest
from katas.stock_trader_v2 import max_profit  # Adjust the path if needed

class TestMaxProfitMultiple(unittest.TestCase):
    def test_example_case(self):
        self.assertEqual(max_profit([7, 1, 5, 3, 6, 4]), 7)

    def test_all_increasing(self):
        self.assertEqual(max_profit([1, 2, 3, 4, 5]), 4)  # profit = 1+1+1+1

    def test_all_decreasing(self):
        self.assertEqual(max_profit([7, 6, 4, 3, 1]), 0)  # no profit

    def test_single_day(self):
        self.assertEqual(max_profit([3]), 0)

    def test_two_days_profit(self):
        self.assertEqual(max_profit([1, 5]), 4)

    def test_two_days_loss(self):
        self.assertEqual(max_profit([5, 1]), 0)

    def test_alternating_up_down(self):
        self.assertEqual(max_profit([1, 3, 2, 4, 3, 5]), 6)  # 2+2+2

    def test_flat_prices(self):
        self.assertEqual(max_profit([3, 3, 3, 3]), 0)