"""
Solution for LC#240: Search a 2D Matrix II
https://leetcode.com/problems/search-a-2d-matrix-ii/
"""
import unittest

# Time complexity: O(M log N) as we do a binary search for each row.
# Space complexity: O(1) no extra structure is used to find the target number.


def binary_search(array: list, desired_number: int) -> bool:
    array_length = len(array)
    pointer_left = 0
    pointer_right = array_length - 1

    while pointer_left <= pointer_right:
        middle_pointer = (pointer_left + pointer_right) // 2
        value = array[middle_pointer]
        if value == desired_number:
            return True
        if value < desired_number:
            pointer_left = middle_pointer + 1
        else:
            pointer_right = middle_pointer - 1


class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        for line in matrix:
            if binary_search(line, target):
                return True
        return False


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_example_1(self):
        matrix = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]]
        target = 5
        self.assertEqual(True, self.solution.searchMatrix(matrix, target))

    def test_example_2(self):
        matrix = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]]
        target = 20
        self.assertEqual(False, self.solution.searchMatrix(matrix, target))
