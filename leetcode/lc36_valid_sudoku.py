"""
Solution for LC#36: Valid Sudoku
https://leetcode.com/problems/valid-sudoku/
"""
import unittest

from collections import defaultdict


class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        board_size = len(board)
        row_store = defaultdict(set)
        column_store = defaultdict(set)
        grid_store = defaultdict(set)

        for row in range(board_size):
            for column in range(board_size):
                cell_value = board[row][column]
                if not cell_value.isdigit():
                    continue
                invalid_row = cell_value in row_store[row]
                invalid_column = cell_value in column_store[column]
                grid_row, grid_column = row // 3, column // 3
                invalid_grid = cell_value in grid_store[(grid_row, grid_column)]
                if invalid_row or invalid_column or invalid_grid:
                    return False
                row_store[row].add(cell_value)
                column_store[column].add(cell_value)
                grid_store[(grid_row, grid_column)].add(cell_value)

        return True


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_example_1(self):
        board = [
            ["5", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"],
        ]
        self.assertEqual(True, self.solution.isValidSudoku(board))

    def test_example_2(self):
        board = [
            ["8", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"],
        ]
        self.assertEqual(False, self.solution.isValidSudoku(board))

    def test_example_3(self):
        board = [
            [".", ".", ".", ".", "5", ".", ".", "1", "."],
            [".", "4", ".", "3", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", "3", ".", ".", "1"],
            ["8", ".", ".", ".", ".", ".", ".", "2", "."],
            [".", ".", "2", ".", "7", ".", ".", ".", "."],
            [".", "1", "5", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", "2", ".", ".", "."],
            [".", "2", ".", "9", ".", ".", ".", ".", "."],
            [".", ".", "4", ".", ".", ".", ".", ".", "."],
        ]
        self.assertEqual(False, self.solution.isValidSudoku(board))

    def test_example_4(self):
        board = [
            [".", "8", "7", "6", "5", "4", "3", "2", "1"],
            ["2", ".", ".", ".", ".", ".", ".", ".", "."],
            ["3", ".", ".", ".", ".", ".", ".", ".", "."],
            ["4", ".", ".", ".", ".", ".", ".", ".", "."],
            ["5", ".", ".", ".", ".", ".", ".", ".", "."],
            ["6", ".", ".", ".", ".", ".", ".", ".", "."],
            ["7", ".", ".", ".", ".", ".", ".", ".", "."],
            ["8", ".", ".", ".", ".", ".", ".", ".", "."],
            ["9", ".", ".", ".", ".", ".", ".", ".", "."],
        ]
        self.assertEqual(True, self.solution.isValidSudoku(board))
