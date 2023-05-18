"""
Solution for LC#695: Max Area of Island
https://leetcode.com/problems/max-area-of-island/
"""
import unittest


class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        number_of_rows = len(grid)
        number_of_columns = len(grid[0])
        island_area = 1
        island_area_counter = 0

        for row in range(number_of_rows):
            for column in range(number_of_columns):
                area = grid[row][column]
                island_counter = 0
                if area == island_area:
                    island_counter += 1
                    left, up, right, down = (row, column - 1), (row - 1, column), (row, column + 1), (row + 1, column)
                    cells = [left, up, right, down]
                    checked = [(row, column)]
                    while cells:
                        cell = cells.pop()
                        if cell not in checked:
                            checked.append(cell)
                            x, y = cell
                            if number_of_rows > x >= 0 and number_of_columns > y >= 0:
                                found_area = grid[x][y]
                                if found_area == island_area:
                                    island_counter += 1
                                    cells += [(x, y - 1), (x - 1, y), (x, y + 1), (x + 1, y)]
                island_area_counter = max(island_area_counter, island_counter)

        return island_area_counter


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
