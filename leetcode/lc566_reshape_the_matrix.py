"""
Solution for LC#566: Reshape the Matrix
https://leetcode.com/problems/reshape-the-matrix/
"""
import unittest


class Solution:
    def matrixReshape(self, mat: list[list[int]], r: int, c: int) -> list[list[int]]:
        number_of_items_in_matrix = 0
        total_items_from_r_and_c = r * c
        items = []
        for row in mat:
            number_of_items_in_matrix += len(row)
            items += row
        if number_of_items_in_matrix != total_items_from_r_and_c:
            return mat

        items_index = 0
        reshaped_matrix = []
        for row in range(r):
            reshaped_matrix.append([])
            for _ in range(c):
                value_from_matrix = items[items_index]
                reshaped_matrix[row].append(value_from_matrix)
                items_index += 1

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
