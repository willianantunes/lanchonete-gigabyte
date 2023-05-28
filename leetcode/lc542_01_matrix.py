"""
Solution for LC#542: 01 Matrix
https://leetcode.com/problems/01-matrix/
"""
import sys
import unittest


class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        number_of_rows = len(mat)
        number_of_column = len(mat[0])

        new_matrix = []

        for row_index in range(number_of_rows):
            new_matrix.append([])
            for column_index in range(number_of_column):
                if mat[row_index][column_index] == 0:
                    new_matrix[row_index].append(0)
                else:
                    new_matrix[row_index].append(sys.maxsize)
                    for r in range(number_of_rows):
                        for c in range(number_of_column):
                            if mat[r][c] == 0:
                                current_value = new_matrix[row_index][column_index]
                                row_distance = abs(r - row_index)
                                column_distance = abs(c - column_index)
                                current_distance_from_the_zero = row_distance + column_distance
                                new_value = min(current_value, current_distance_from_the_zero)
                                new_matrix[row_index][column_index] = new_value
        return new_matrix


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_example_1(self):
        mat = [
            [0, 0, 0],
            [0, 1, 0],
            [0, 0, 0],
        ]
        self.assertEqual(
            [
                [0, 0, 0],
                [0, 1, 0],
                [0, 0, 0],
            ],
            self.solution.updateMatrix(mat),
        )

    def test_example_2(self):
        mat = [
            [0, 0, 0],
            [0, 1, 0],
            [1, 1, 1],
        ]
        self.assertEqual(
            [
                [0, 0, 0],
                [0, 1, 0],
                [1, 2, 1],
            ],
            self.solution.updateMatrix(mat),
        )

    def test_example_3(self):
        mat = [
            [0, 1, 0],
            [1, 1, 0],
            [1, 1, 1],
        ]
        self.assertEqual(
            [
                [0, 1, 0],
                [1, 1, 0],
                [2, 2, 1],
            ],
            self.solution.updateMatrix(mat),
        )

    def test_example_4(self):
        mat = [
            [0, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 0, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 0],
        ]
        self.assertEqual(
            [
                [0, 1, 2, 3, 3, 2, 1, 2],
                [1, 2, 3, 3, 2, 1, 0, 1],
                [2, 3, 3, 4, 3, 2, 1, 2],
                [3, 3, 2, 3, 4, 3, 2, 3],
                [3, 2, 1, 2, 3, 4, 3, 3],
                [2, 1, 0, 1, 2, 3, 3, 2],
                [3, 2, 1, 2, 3, 3, 2, 1],
                [4, 3, 2, 3, 3, 2, 1, 0],
            ],
            self.solution.updateMatrix(mat),
        )
