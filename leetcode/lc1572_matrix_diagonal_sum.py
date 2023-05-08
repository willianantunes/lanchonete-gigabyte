"""
Solution for LC#1572: Matrix Diagonal Sum
https://leetcode.com/problems/matrix-diagonal-sum/
"""
import unittest


class Solution:
    def diagonalSum(self, mat: list[list[int]]) -> int:
        number_of_rows = len(mat)
        number_of_columns = len(mat[0]) - 1
        primary_diagonal = secondary_diagonal = 0
        for row in range(number_of_rows):
            primary_diagonal += mat[row][row]
            if row != number_of_columns:
                secondary_diagonal += mat[row][number_of_columns]
            number_of_columns -= 1
        return primary_diagonal + secondary_diagonal


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_example_1(self):
        mat = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
        ]
        self.assertEqual(25, self.solution.diagonalSum(mat))

    def test_example_2(self):
        mat = [
            [1, 1, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 1, 1],
        ]
        self.assertEqual(8, self.solution.diagonalSum(mat))

    def test_example_3(self):
        mat = [[5]]
        self.assertEqual(5, self.solution.diagonalSum(mat))
