"""
Solution for LC#200: Number of Islands
https://leetcode.com/problems/number-of-islands/
"""
import unittest


class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        number_of_rows = len(grid)
        number_of_columns = len(grid[0])

        island_counter = 0

        def _clear_adjacent_islands(row, column):
            if number_of_rows > row >= 0 and number_of_columns > column >= 0 and grid[row][column] == "1":
                grid[row][column] = "0"
                _clear_adjacent_islands(row + 1, column)
                _clear_adjacent_islands(row - 1, column)
                _clear_adjacent_islands(row, column + 1)
                _clear_adjacent_islands(row, column - 1)

            return

        for row_index in range(number_of_rows):
            for column_index in range(number_of_columns):
                if grid[row_index][column_index] == "1":
                    island_counter += 1
                    _clear_adjacent_islands(row_index, column_index)

        return island_counter


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_example_1(self):
        grid = [
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"],
        ]
        self.assertEqual(1, self.solution.numIslands(grid))

    def test_example_2(self):
        grid = [
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"],
        ]
        self.assertEqual(3, self.solution.numIslands(grid))
