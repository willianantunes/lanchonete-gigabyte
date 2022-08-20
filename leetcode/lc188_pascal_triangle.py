"""
Solution for LC#118: Pascal's Triangle
https://leetcode.com/problems/pascals-triangle/
"""
import unittest


class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        triangle = []

        for row in range(1, numRows + 1):
            for entry in range(row):
                if entry == 0:
                    triangle.append([])
                for column in range(row):
                    if column == 0 or column == row - 1:
                        triangle[row - 1].append(1)
                    else:
                        sum_two_numbers = triangle[row - 2][column - 1] + triangle[row - 2][column]
                        triangle[row - 1].append(sum_two_numbers)
                break

        return triangle


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_example_1(self):
        numRows = 5
        self.assertEqual([[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]], self.solution.generate(numRows))

    def test_example_2(self):
        numRows = 1
        self.assertEqual([[1]], self.solution.generate(numRows))
