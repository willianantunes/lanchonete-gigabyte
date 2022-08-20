"""
Solution for LC#74: Search a 2D Matrix
https://leetcode.com/problems/search-a-2d-matrix/
"""
import unittest

from typing import Union


def binary_search(ordered_array, target_value) -> Union[bool, int]:
    y_values_size = len(ordered_array)
    left = 0
    right = y_values_size - 1

    while left <= right:
        middle = int((left + right) / 2)
        if target_value == ordered_array[middle]:
            return True
        if target_value > ordered_array[middle]:
            left = middle + 1
        else:
            right = middle - 1

    return right


class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        matrix_size = len(matrix)
        if matrix_size == 1:
            result = binary_search(matrix[0], target)
            if result is True:
                return True
            return False

        y_values = []
        for row in matrix:
            y_values.append(row[0])

        result = binary_search(y_values, target)
        if result is True:
            return True

        x_values = matrix[result]

        result = binary_search(x_values, target)
        if result is True:
            return True

        return False


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_example_1(self):
        matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
        target = 3
        self.assertEqual(True, self.solution.searchMatrix(matrix, target))

    def test_example_2(self):
        matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
        target = 13
        self.assertEqual(False, self.solution.searchMatrix(matrix, target))

    def test_example_3(self):
        matrix = [[1, 2], [3, 5]]
        target = 2
        self.assertEqual(True, self.solution.searchMatrix(matrix, target))

    def test_example_4(self):
        matrix = [[1, 2], [3, 5]]
        target = 5
        self.assertEqual(True, self.solution.searchMatrix(matrix, target))

    def test_example_5(self):
        matrix = [[1, 3]]
        target = 3
        self.assertEqual(True, self.solution.searchMatrix(matrix, target))

    def test_example_6(self):
        matrix = [[1, 3]]
        target = 5
        self.assertEqual(False, self.solution.searchMatrix(matrix, target))
