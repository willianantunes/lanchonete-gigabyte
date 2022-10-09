"""
Solution for LC#59: Spiral Matrix II
https://leetcode.com/problems/spiral-matrix-ii/
"""
import unittest

from dataclasses import dataclass

# Time complexity: O(NxN) as each cell is configured to set its value.
# Space complexity: O(NxN) as we create a matrix to store the values.
# We also use extra space to create the state direction thing, but it's fixed and does not change,
# so we can ignore it.


@dataclass
class StateDirection:
    is_row_fixed: bool
    increase: bool
    next_state: "StateDirection" = None


class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        number_of_rows = number_of_column = n
        total_number_of_cells = number_of_rows * number_of_column

        # States about each direction
        # Circular list
        left_up = StateDirection(is_row_fixed=False, increase=False)
        down_left = StateDirection(is_row_fixed=True, increase=False, next_state=left_up)
        right_down = StateDirection(is_row_fixed=False, increase=True, next_state=down_left)
        up_right = StateDirection(is_row_fixed=True, increase=True, next_state=right_down)
        # To make the linked objects circular
        left_up.next_state = up_right

        visited = []
        current_state = up_right
        current_row = current_column = 0
        change_direction = False
        counter = 1
        result = [[None for _ in range(number_of_column)] for _ in range(number_of_rows)]

        while True:
            invalid_current_column = current_column > number_of_column - 1 or current_column < 0
            invalid_current_row = current_row > number_of_rows - 1 or current_row < 0
            if invalid_current_column or invalid_current_row:
                change_direction = True
            tuple_of_indexes = (current_row, current_column)
            if not change_direction and tuple_of_indexes not in visited:
                result[current_row][current_column] = counter
                if counter == total_number_of_cells:
                    break
                counter += 1
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

        return result


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_example_1(self):
        n = 3
        self.assertEqual([[1, 2, 3], [8, 9, 4], [7, 6, 5]], self.solution.generateMatrix(n))

    def test_example_2(self):
        n = 1
        self.assertEqual([[1]], self.solution.generateMatrix(n))
