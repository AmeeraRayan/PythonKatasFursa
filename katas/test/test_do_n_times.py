import unittest
from unittest.mock import Mock ##silent tally counter
from katas.do_n_times import do_n_times

class TestDoNTimes(unittest.TestCase):
    def test_called_five_times(self):
        mock_func = Mock()
        do_n_times(mock_func, 5)
        self.assertEqual(mock_func.call_count, 5)

    def test_called_once(self):
        mock_func = Mock()
        do_n_times(mock_func, 1)
        self.assertEqual(mock_func.call_count, 1)

    def test_called_zero_times(self):
        mock_func = Mock()
        do_n_times(mock_func, 0)
        self.assertEqual(mock_func.call_count, 0)
