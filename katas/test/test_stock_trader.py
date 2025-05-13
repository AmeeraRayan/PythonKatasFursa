import unittest
from katas.stock_trader import max_profit  # Adjust the import path if needed

class TestMaxProfit(unittest.TestCase):
    def test_example_case(self):
        self.assertEqual(max_profit([7, 1, 5, 3, 6, 4]), 5)

    def test_no_profit_possible(self):
        self.assertEqual(max_profit([7, 6, 4, 3, 1]), 0)

    def test_always_increasing(self):
        self.assertEqual(max_profit([1, 2, 3, 4, 5]), 4)

    def test_always_decreasing(self):
        self.assertEqual(max_profit([9, 8, 7, 6, 5]), 0)

    def test_single_day(self):
        self.assertEqual(max_profit([3]), 0)

    def test_two_days_profit(self):
        self.assertEqual(max_profit([1, 5]), 4)

    def test_two_days_loss(self):
        self.assertEqual(max_profit([5, 1]), 0)

    def test_empty_list(self):
        self.assertEqual(max_profit([]), 0)

    def test_buy_low_sell_high_late(self):
        self.assertEqual(max_profit([9, 1, 2, 10, 1, 3]), 9)  # Buy at 1, sell at 10