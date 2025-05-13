import unittest
from katas.requirements_coverage import select_minimal_test_cases  # Adjust the path if needed

class TestRequirementsCoverage(unittest.TestCase):
    def test_example_case(self):
        test_cases = [
            [1, 2, 3],
            [1, 4],
            [2, 3, 4],
            [1, 5],
            [3, 5]
        ]
        result = select_minimal_test_cases(test_cases)
        self.assertEqual(set(result), {2, 3})

    def test_minimal_all_unique(self):
        test_cases = [
            [1],
            [2],
            [3],
            [4],
            [5]
        ]
        result = select_minimal_test_cases(test_cases)
        self.assertEqual(set(result), {0, 1, 2, 3, 4})

    def test_full_overlap(self):
        test_cases = [
            [1, 2, 3, 4, 5],
            [1],
            [2],
            [3],
            [4],
            [5]
        ]
        result = select_minimal_test_cases(test_cases)
        self.assertEqual(set(result), {0})

    def test_multiple_valid_solutions(self):
        test_cases = [
            [1, 2],
            [3, 4],
            [1, 3],
            [2, 4]
        ]
        result = select_minimal_test_cases(test_cases)
        # There are two valid answers: [0, 1] or [2, 3]
        self.assertIn(set(result), [{0, 1}, {2, 3}])

    def test_empty_case(self):
        result = select_minimal_test_cases([])
        self.assertEqual(result, [])