import unittest
from katas.longest_common_prefix import longest_common_prefix  # Adjust path if needed

class TestLongestCommonPrefix(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(longest_common_prefix(["flower", "flow", "flight"]), "fl")

    def test_example2(self):
        self.assertEqual(longest_common_prefix(["dog", "racecar", "car"]), "")

    def test_example3(self):
        self.assertEqual(longest_common_prefix(["interspecies", "interstellar", "interstate"]), "inters")

    def test_example4(self):
        self.assertEqual(longest_common_prefix(["apple", "apricot", "ape"]), "ap")

    def test_single_word(self):
        self.assertEqual(longest_common_prefix(["hello"]), "hello")

    def test_empty_list(self):
        self.assertEqual(longest_common_prefix([]), "")

    def test_no_common_prefix(self):
        self.assertEqual(longest_common_prefix(["a", "b", "c"]), "")

    def test_all_same_words(self):
        self.assertEqual(longest_common_prefix(["same", "same", "same"]), "same")
