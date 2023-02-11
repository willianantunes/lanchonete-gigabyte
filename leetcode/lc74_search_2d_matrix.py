"""
Solution for LC#74: Search a 2D Matrix
https://leetcode.com/problems/search-a-2d-matrix/
"""
import bisect
import unittest


def binary_search(array, target) -> bool:
    index = bisect.bisect_left(array, target)
    if index < len(array) and array[index] == target:
        return True
    return False


class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        number_of_rows = len(matrix)
        if number_of_rows == 1:
            return binary_search(matrix[0], target)

        previous_row = 0
        chosen_row = None
        for current_row in range(1, number_of_rows):
            previous_first_cell_value = matrix[previous_row][0]
            current_first_cell_value = matrix[current_row][0]
            if previous_first_cell_value <= target < current_first_cell_value:
                chosen_row = previous_row
                break
            previous_row += 1
            chosen_row = current_row

        return binary_search(matrix[chosen_row], target)


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
