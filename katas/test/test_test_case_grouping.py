import unittest
from katas.test_case_grouping import group_test_cases  # Update the path if needed

class TestGroupTestCases(unittest.TestCase):
    def is_valid_grouping(self, sizes, result):
        """Helper to validate the grouping result."""
        used = []
        for group in result:
            expected_size = sizes[group[0]]
            if len(group) != expected_size:
                return False
            for idx in group:
                if sizes[idx] != expected_size or idx in used:
                    return False
                used.append(idx)
        return sorted(used) == list(range(len(sizes)))

    def test_example_case(self):
        sizes = [1, 2, 3, 3, 3, 2]
        result = group_test_cases(sizes)
        self.assertTrue(self.is_valid_grouping(sizes, result))

    def test_simple_case(self):
        sizes = [2, 2, 1, 1]
        result = group_test_cases(sizes)
        self.assertTrue(self.is_valid_grouping(sizes, result))

    def test_all_groups_of_one(self):
        sizes = [1, 1, 1]
        result = group_test_cases(sizes)
        self.assertEqual(len(result), 3)
        self.assertTrue(self.is_valid_grouping(sizes, result))

    def test_single_group(self):
        sizes = [4, 4, 4, 4]
        result = group_test_cases(sizes)
        self.assertEqual(len(result), 1)
        self.assertEqual(len(result[0]), 4)

    def test_multiple_groups_same_size(self):
        sizes = [2, 2, 2, 2, 2, 2]
        result = group_test_cases(sizes)
        self.assertEqual(len(result), 3)
        for group in result:
            self.assertEqual(len(group), 2)

    def test_empty_list(self):
        sizes = []
        result = group_test_cases(sizes)
        self.assertEqual(result, [])