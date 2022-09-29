"""
Solution for LC#119: Pascal's Triangle II
https://leetcode.com/problems/pascals-triangle-ii/
"""
import unittest


class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        array = [1 for _ in range(rowIndex + 1)]

        for number_of_interactions in range(2, rowIndex + 1):
            start = number_of_interactions - 1
            for current_position in range(start, 0, -1):
                previous_position = current_position - 1
                value = array[previous_position]
                array[current_position] += value

        return array


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_example_1(self):
        rowIndex = 3
        self.assertEqual([1, 3, 3, 1], self.solution.getRow(rowIndex))

    def test_example_2(self):
        rowIndex = 0
        self.assertEqual([1], self.solution.getRow(rowIndex))

    def test_example_3(self):
        rowIndex = 1
        self.assertEqual([1, 1], self.solution.getRow(rowIndex))

    def test_example_4(self):
        rowIndex = 7
        self.assertEqual([1, 7, 21, 35, 35, 21, 7, 1], self.solution.getRow(rowIndex))

    def test_example_5(self):
        rowIndex = 4
        self.assertEqual([1, 4, 6, 4, 1], self.solution.getRow(rowIndex))

    def test_example_6(self):
        rowIndex = 5
        self.assertEqual([1, 5, 10, 10, 5, 1], self.solution.getRow(rowIndex))

    def test_example_7(self):
        rowIndex = 6
        self.assertEqual([1, 6, 15, 20, 15, 6, 1], self.solution.getRow(rowIndex))
