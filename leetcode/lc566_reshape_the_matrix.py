"""
Solution for LC#566: Reshape the Matrix
https://leetcode.com/problems/reshape-the-matrix/
"""
import unittest


class Solution:
    def matrixReshape(self, mat: list[list[int]], r: int, c: int) -> list[list[int]]:
        number_of_rows = len(mat)
        number_of_columns = len(mat[0])
        total_cells = number_of_rows * number_of_columns
        is_illegal = total_cells != r * c
        if is_illegal:
            return mat

        mat_row_index = mat_column_index = 0
        reshaped_matrix = []
        for row_index in range(r):
            reshaped_matrix.append([])
            for column_index in range(c):
                value = mat[mat_row_index][mat_column_index]
                reshaped_matrix[row_index].append(value)
                mat_column_index += 1
                if mat_column_index == number_of_columns:
                    mat_column_index = 0
                    mat_row_index += 1

        return reshaped_matrix


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_example_1(self):
        mat = [[1, 2], [3, 4]]
        r = 1
        c = 4
        self.assertEqual([[1, 2, 3, 4]], self.solution.matrixReshape(mat, r, c))

    def test_example_2(self):
        mat = [[1, 2], [3, 4]]
        r = 2
        c = 4
        self.assertEqual([[1, 2], [3, 4]], self.solution.matrixReshape(mat, r, c))
