import unittest
from katas.semantic_version_comparator import compare_versions  # Adjust the path if needed

class TestCompareVersions(unittest.TestCase):
    def test_less_than(self):
        self.assertEqual(compare_versions("1.0.0", "1.0.1"), -1)
        self.assertEqual(compare_versions("1.2.0", "1.2.3"), -1)
        self.assertEqual(compare_versions("1.2", "1.2.1"), -1)
        self.assertEqual(compare_versions("2.0.0", "10.0.0"), -1)

    def test_greater_than(self):
        self.assertEqual(compare_versions("2.1.0", "1.9.9"), 1)
        self.assertEqual(compare_versions("1.10.0", "1.2.0"), 1)
        self.assertEqual(compare_versions("1.2.1", "1.2"), 1)

    def test_equal_versions(self):
        self.assertEqual(compare_versions("1.2.3", "1.2.3"), 0)
        self.assertEqual(compare_versions("1.2", "1.2.0"), 0)
        self.assertEqual(compare_versions("1.0.0", "1"), 0)
        self.assertEqual(compare_versions("0.0.0", "0.0"), 0)

    def test_leading_zeros(self):
        self.assertEqual(compare_versions("01.02.03", "1.2.3"), 0)
        self.assertEqual(compare_versions("1.2.03", "1.2.3"), 0)