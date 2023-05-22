"""
Solution for LC#695: Max Area of Island
https://leetcode.com/problems/max-area-of-island/
"""
import unittest


class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        number_of_rows = len(grid)
        number_of_columns = len(grid[0])

        def _dfs(row, column):
            if number_of_rows > row >= 0 and number_of_columns > column >= 0 and grid[row][column] == 1:
                grid[row][column] = 0
                return 1 + _dfs(row + 1, column) + _dfs(row - 1, column) + _dfs(row, column + 1) + _dfs(row, column - 1)

            return 0

        bigger_island = 0
        for row_index in range(number_of_rows):
            for column_index in range(number_of_columns):
                if grid[row_index][column_index] == 1:
                    area = _dfs(row_index, column_index)
                    bigger_island = max(bigger_island, area)

        return bigger_island


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_example_1(self):
        grid = [
            [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
        ]
        self.assertEqual(6, self.solution.maxAreaOfIsland(grid))

    def test_example_2(self):
        grid = grid = [[0, 0, 0, 0, 0, 0, 0, 0]]
        self.assertEqual(0, self.solution.maxAreaOfIsland(grid))
