"""
Solution for LC#994: Rotting Oranges
https://leetcode.com/problems/rotting-oranges/
"""
import unittest

from collections import deque


class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        fresh_orange, rotten_orange = 1, 2
        number_of_rows = len(grid)
        number_of_columns = len(grid[0])
        number_of_fresh_orange = 0
        queue = deque([])

        for row_index in range(number_of_rows):
            for column_index in range(number_of_columns):
                cell_value = grid[row_index][column_index]
                if cell_value == fresh_orange:
                    number_of_fresh_orange += 1
                elif cell_value == rotten_orange:
                    queue.appendleft((row_index, column_index))

        if number_of_fresh_orange == 0 and queue:
            return 0
        if number_of_fresh_orange != 0 and not queue:
            return -1

        minutes = 0
        four_neighbor_pixels = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while queue:
            rotten_oranges = list(queue)
            queue.clear()
            increase_minute = False
            for rotten_row, rotten_column in rotten_oranges:
                for neighbor_index in range(len(four_neighbor_pixels)):
                    target_row = rotten_row + four_neighbor_pixels[neighbor_index][0]
                    target_column = rotten_column + four_neighbor_pixels[neighbor_index][1]
                    valid_target = number_of_rows > target_row >= 0 and number_of_columns > target_column >= 0
                    if valid_target:
                        is_fresh_orange = grid[target_row][target_column] == fresh_orange
                        if is_fresh_orange:
                            grid[target_row][target_column] = rotten_orange
                            queue.appendleft((target_row, target_column))
                            number_of_fresh_orange -= 1
                            increase_minute = True
            if increase_minute:
                minutes += 1

        if number_of_fresh_orange == 0:
            return minutes

        return -1


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_example_1(self):
        grid = [
            [2, 1, 1],
            [1, 1, 0],
            [0, 1, 1],
        ]
        self.assertEqual(4, self.solution.orangesRotting(grid))

    def test_example_2(self):
        grid = [
            [2, 1, 1],
            [0, 1, 1],
            [1, 0, 1],
        ]
        self.assertEqual(-1, self.solution.orangesRotting(grid))

    def test_example_3(self):
        grid = [
            [0, 2],
        ]
        self.assertEqual(0, self.solution.orangesRotting(grid))

    def test_example_4(self):
        grid = [
            [1],
        ]
        self.assertEqual(-1, self.solution.orangesRotting(grid))

    def test_example_5(self):
        grid = [
            [2, 1, 1],
            [1, 1, 1],
            [0, 1, 2],
        ]
        self.assertEqual(2, self.solution.orangesRotting(grid))
