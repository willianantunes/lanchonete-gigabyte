"""
Solution for LC#74: Search a 2D Matrix
https://leetcode.com/problems/search-a-2d-matrix/
"""
import unittest

from typing import Union


def binary_search(desired_number, ordered_array) -> bool:
    list_size = len(ordered_array)
    left = 0
    right = list_size - 1

    while left <= right:
        middle = (left + right) // 2
        value = ordered_array[middle]
        if value == desired_number:
            return True
        elif value < desired_number:
            left = middle + 1
        else:
            right = middle - 1

    return False


class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        matrix_size = len(matrix)
        fixed_column = 0
        chosen_row = last_value = None
        for row in range(matrix_size):
            value = matrix[row][fixed_column]
            if row == 0:
                chosen_row = row - 1
                last_value = value
                continue
            if target < value and target >= last_value:
                chosen_row = row - 1
                break
            chosen_row = row
            last_value = value

        target_list = matrix[chosen_row]

        return binary_search(target, target_list)


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
