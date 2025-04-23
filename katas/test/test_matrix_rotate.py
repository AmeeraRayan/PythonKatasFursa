import unittest
from katas.matrix_rotate import rotate_matrix

class TestRotateMatrix(unittest.TestCase):
    def test_3x3_matrix(self):
        matrix = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        rotate_matrix(matrix)
        self.assertEqual(matrix, [
            [7, 4, 1],
            [8, 5, 2],
            [9, 6, 3]
        ])

    def test_2x2_matrix(self):
        matrix = [
            [1, 2],
            [3, 4]
        ]
        rotate_matrix(matrix)
        self.assertEqual(matrix, [
            [3, 1],
            [4, 2]
        ])
