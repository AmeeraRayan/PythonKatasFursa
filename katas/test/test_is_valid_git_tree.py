import unittest
from katas.is_valid_git_tree import is_valid_git_tree  # עדכני את הנתיב אם צריך

class TestIsValidGitTree(unittest.TestCase):
    def test_valid_tree(self):
        tree = {
            "A": ["B", "C"],
            "B": ["D"],
            "C": [],
            "D": []
        }
        self.assertTrue(is_valid_git_tree(tree))  # אמור להיות True

    def test_tree_with_cycle(self):
        tree = {
            "A": ["B"],
            "B": ["C"],
            "C": ["A"]  # יש מעגל
        }
        self.assertFalse(is_valid_git_tree(tree))

    def test_multiple_roots(self):
        tree = {
            "A": [],
            "B": []
        }
        self.assertFalse(is_valid_git_tree(tree))  # שני שורשים

    def test_disconnected_node(self):
        tree = {
            "A": ["B"],
            "B": [],
            "C": []  # C מנותק
        }
        self.assertFalse(is_valid_git_tree(tree))

    def test_single_node(self):
        tree = {
            "A": []
        }
        self.assertTrue(is_valid_git_tree(tree))  # קומיט אחד זה עץ חוקי

    def test_empty_tree(self):
        tree = {}
        self.assertFalse(is_valid_git_tree(tree))  # אין שום קומיט בכלל