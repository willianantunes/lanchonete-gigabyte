"""
Solution for LC#118: Pascal's Triangle
https://leetcode.com/problems/pascals-triangle/
"""
import unittest


class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        pascal_triangle = []

        for line in range(numRows):
            pascal_triangle.append([])
            number_of_cells = line + 1
            for column in range(number_of_cells):
                is_number_the_limit = column == 0 or column == number_of_cells - 1
                if is_number_the_limit:
                    pascal_triangle[line].append(1)
                else:
                    above_left = pascal_triangle[line - 1][column - 1]
                    above_right = pascal_triangle[line - 1][column]
                    sum_two_numbers_above = above_left + above_right
                    pascal_triangle[line].append(sum_two_numbers_above)

        return pascal_triangle


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_example_1(self):
        numRows = 5
        self.assertEqual([[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]], self.solution.generate(numRows))

    def test_example_2(self):
        numRows = 1
        self.assertEqual([[1]], self.solution.generate(numRows))
