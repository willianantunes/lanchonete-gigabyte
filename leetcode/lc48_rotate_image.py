"""
Solution for LC#48: Rotate Image
https://leetcode.com/problems/rotate-image/
"""
import unittest

# Time complexity : O(M*2) as each cell is read once to create a copy matrix and then another time to do the in-place.
# Space complexity : O(M) because we create a copy of the received matrix during the process.


class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        matrix_size = len(matrix)
        matrix_copy = []
        for row in range(matrix_size):
            matrix_copy.append([])
            for column in range(matrix_size):
                matrix_copy[row].append(matrix[row][column])

        for row in range(matrix_size):
            position_to_be_placed = (matrix_size - 1) - row
            for column in range(matrix_size):
                matrix[column][position_to_be_placed] = matrix_copy[row][column]


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_example_1(self):
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.solution.rotate(matrix)
        self.assertEqual([[7, 4, 1], [8, 5, 2], [9, 6, 3]], matrix)

    def test_example_2(self):
        matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
        self.solution.rotate(matrix)
        self.assertEqual([[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]], matrix)
