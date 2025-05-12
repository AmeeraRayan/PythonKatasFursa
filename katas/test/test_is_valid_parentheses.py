import unittest
from katas.is_valid_parentheses import is_valid_parentheses  # שנה את הנתיב אם צריך

class TestIsValidParentheses(unittest.TestCase):
    def test_all_correct_types(self):
        self.assertTrue(is_valid_parentheses("()[]{}"))

    def test_incorrect_closing(self):
        self.assertFalse(is_valid_parentheses("(]"))

    def test_wrong_nesting(self):
        self.assertFalse(is_valid_parentheses("([)]"))

    def test_correct_nested(self):
        self.assertTrue(is_valid_parentheses("{[]()}"))

    def test_empty_string(self):
        self.assertTrue(is_valid_parentheses(""))

    def test_only_opening(self):
        self.assertFalse(is_valid_parentheses("((("))

    def test_only_closing(self):
        self.assertFalse(is_valid_parentheses(")))"))

    def test_extra_opening(self):
        self.assertFalse(is_valid_parentheses("(()"))

    def test_extra_closing(self):
        self.assertFalse(is_valid_parentheses("())"))

    def test_long_valid(self):
        self.assertTrue(is_valid_parentheses("[({({[]})})]"))