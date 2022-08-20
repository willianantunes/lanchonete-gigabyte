"""
Solution for LC#36: Valid Sudoku
https://leetcode.com/problems/valid-sudoku/
"""
import unittest


class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        board_size = len(board)

        def is_line_valid(fixed_position, retrieve_cell_value_callable):
            counter_entries = {}
            for index in range(board_size):
                cell_value = retrieve_cell_value_callable(fixed_position, index)
                if cell_value != ".":
                    counter = counter_entries.get(cell_value, 0) + 1
                    counter_entries[cell_value] = counter
                    if counter > 1:
                        return False
            return True

        for row in range(board_size):
            valid_row = is_line_valid(row, lambda fixed_position, index: board[fixed_position][index])
            if not valid_row:
                return False
            row_as_column = row
            valid_column = is_line_valid(row_as_column, lambda fixed_position, index: board[index][fixed_position])
            if not valid_column:
                return False
            evaluate_boxes = (row + 1) % 3 == 0
            if evaluate_boxes:
                pointer = row
                for lap, box_position in enumerate(range(0, 3)):
                    box_start = (pointer + 1) - 3
                    box_stop = pointer + 1
                    interactions = 0
                    counter_entries = {}
                    for box_row in range(box_start, box_stop, 1):
                        for box_column in range(0, 3):
                            interactions += 1
                            box_column = box_column if lap == 0 else box_column + (3 * box_position)
                            cell_value = board[box_row][box_column]
                            if cell_value != ".":
                                counter = counter_entries.get(cell_value, 0) + 1
                                counter_entries[cell_value] = counter
                                if counter > 1:
                                    return False
                        if interactions % 9 == 0:
                            counter_entries = {}
                            interactions = 0

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
