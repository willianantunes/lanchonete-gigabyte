"""
Solution for LC#54: Spiral Matrix
https://leetcode.com/problems/spiral-matrix/
"""
import unittest

from dataclasses import dataclass

# Time complexity: O(MxN) as each cell is accessed once to retrieve its value.
# Space complexity: O(MxN) as we return a list containing all the values contained in the matrix.
# We also use extra space to create the state direction thing, but it's fixed and does not change,
# so we can ignore it.


@dataclass
class StateDirection:
    is_row_fixed: bool
    increase: bool
    next_state: "StateDirection" = None


class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        visited = []
        number_of_rows = len(matrix)
        number_of_column = len(matrix[0])
        total_number_of_cells = number_of_rows * number_of_column

        # States about each direction
        # Circular list
        left_up = StateDirection(is_row_fixed=False, increase=False)
        down_left = StateDirection(is_row_fixed=True, increase=False, next_state=left_up)
        right_down = StateDirection(is_row_fixed=False, increase=True, next_state=down_left)
        up_right = StateDirection(is_row_fixed=True, increase=True, next_state=right_down)
        # To make the linked objects circular
        left_up.next_state = up_right

        current_state = up_right
        current_row = current_column = 0
        change_direction = False
        elements_from_spiral = []

        while len(visited) != total_number_of_cells:
            invalid_current_column = current_column > number_of_column - 1 or current_column < 0
            invalid_current_row = current_row > number_of_rows - 1 or current_row < 0
            if invalid_current_column or invalid_current_row:
                change_direction = True
            tuple_of_indexes = (current_row, current_column)
            if not change_direction and tuple_of_indexes not in visited:
                element = matrix[current_row][current_column]
                elements_from_spiral.append(element)
                visited.append(tuple_of_indexes)
            else:
                change_direction = True
            if change_direction:
                if current_state.is_row_fixed:
                    if current_state.increase:
                        current_column -= 1
                        current_row += 1
                    else:
                        current_column += 1
                        current_row -= 1
                else:
                    if current_state.increase:
                        current_column -= 1
                        current_row -= 1
                    else:
                        current_column += 1
                        current_row += 1
                current_state = current_state.next_state
                change_direction = False
            else:
                if current_state.is_row_fixed:
                    current_column = current_column - 1 if not current_state.increase else current_column + 1
                else:
                    current_row = current_row - 1 if not current_state.increase else current_row + 1

        return elements_from_spiral


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_example_1(self):
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertEqual([1, 2, 3, 6, 9, 8, 7, 4, 5], self.solution.spiralOrder(matrix))

    def test_example_2(self):
        matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
        self.assertEqual([1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7], self.solution.spiralOrder(matrix))

    def test_example_3(self):
        matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
        self.assertEqual([1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10], self.solution.spiralOrder(matrix))
