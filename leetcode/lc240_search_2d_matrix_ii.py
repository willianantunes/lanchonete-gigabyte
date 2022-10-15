"""
Solution for LC#240: Search a 2D Matrix II
https://leetcode.com/problems/search-a-2d-matrix-ii/
"""
import unittest

# Time complexity: O(M + N) as the worst case implies reading at most M + N cells.
# Space complexity: O(1) no extra structure is used to find the target number.


class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        number_of_lines = len(matrix)
        number_of_columns = len(matrix[0])
        row_index, column_index = 0, number_of_columns - 1

        while column_index >= 0 and row_index < number_of_lines:
            cell_value = matrix[row_index][column_index]

            decrease_column_index = cell_value > target
            increase_row_index = cell_value < target

            if decrease_column_index:
                column_index -= 1
            elif increase_row_index:
                row_index += 1
            else:
                return True

        return False


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_example_1(self):
        matrix = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]]
        target = 18
        self.assertEqual(True, self.solution.searchMatrix(matrix, target))

    def test_example_2(self):
        matrix = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]]
        target = 20
        self.assertEqual(False, self.solution.searchMatrix(matrix, target))
