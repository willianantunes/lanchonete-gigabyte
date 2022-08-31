"""
Solution for LC#566: Reshape the Matrix
https://leetcode.com/problems/reshape-the-matrix/
"""
import unittest


class Solution:
    def matrixReshape(self, mat: list[list[int]], r: int, c: int) -> list[list[int]]:
        number_of_rows = len(mat)
        number_of_columns = len(mat[0])
        number_of_elements = number_of_rows * number_of_columns
        number_of_elements_desired_reshaped = r * c
        if number_of_elements != number_of_elements_desired_reshaped:
            return mat

        elements = []
        for row in range(number_of_rows):
            for column in range(number_of_columns):
                elements.append(mat[row][column])

        counter = 0
        reshaped = []
        for row in range(r):
            reshaped.append([])
            for column in range(c):
                reshaped[row].append(elements[counter])
                counter += 1

        return reshaped


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
