from typing import List
from itertools import combinations

def select_minimal_test_cases(test_cases: List[List[int]]) -> List[int]:
    """
    In software testing, it's often required to select a minimal set of test cases that cover all the requirements.
    You are given a set of test cases and their associated covered requirements.
    Your task is to select the minimal subset of test cases such that all requirements are covered.

    For example, you have the following test cases and requirements they cover:

    test_cases = [
        [1, 2, 3],   # Test case 0 covers requirements 1, 2, 3
        [1, 4],      # Test case 1 covers requirements 1, 4
        [2, 3, 4],   # Test case 2 covers requirements 2, 3, 4
        [1, 5],      # Test case 3 covers requirements 1, 5
        [3, 5]       # Test case 4 covers requirements 3, 5
    ]

    Args:
        test_cases: a list of test cases, where each test case is a list of requirements it covers.
                    Assume each requirement is covered by at least one test case.

    Returns:
        A list of indices of the minimal subset of test cases that covers all requirements
    """
    # Step 1: Find all unique requirements
    all_requirements = set(req for case in test_cases for req in case)
    n = len(test_cases)

    for r in range(1, n + 1):
        for combo in combinations(range(n), r):
            covered = set()
            for i in combo:
                covered.update(test_cases[i])
            if covered == all_requirements:
                return list(combo)

    return []


if __name__ == "__main__":
    test_cases = [
        [1, 2, 3],
        [1, 4],
        [2, 3, 4],
        [1, 5],
        [3, 5]
    ]

    result = select_minimal_test_cases(test_cases)
    print(result)  # Expected output: [2, 3]
