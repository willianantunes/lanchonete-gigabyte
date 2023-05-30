"""
Solution for LC#542: 01 Matrix
https://leetcode.com/problems/01-matrix/
"""
import sys
import unittest

from collections import deque


class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        number_of_rows = len(mat)
        number_of_column = len(mat[0])

        new_matrix = [[sys.maxsize for _ in range(number_of_column)] for _ in range(number_of_rows)]

        queue = deque([])
        for row_index in range(number_of_rows):
            for column_index in range(number_of_column):
                is_zero_cell = mat[row_index][column_index] == 0
                if is_zero_cell:
                    new_matrix[row_index][column_index] = 0
                    queue.appendleft((row_index, column_index))

        four_neighbor_pixels = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while queue:
            previous_row, previous_column = queue.popleft()
            for neighbor_index in range(len(four_neighbor_pixels)):
                target_row = previous_row + four_neighbor_pixels[neighbor_index][0]
                target_column = previous_column + four_neighbor_pixels[neighbor_index][1]
                are_targets_valid = number_of_rows > target_row >= 0 and number_of_column > target_column >= 0
                if are_targets_valid:
                    new_value = new_matrix[previous_row][previous_column] + 1
                    current_value = new_matrix[target_row][target_column]
                    if current_value > new_value:
                        new_matrix[target_row][target_column] = new_value
                        queue.appendleft((target_row, target_column))

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
