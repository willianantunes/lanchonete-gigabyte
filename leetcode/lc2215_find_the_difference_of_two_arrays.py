"""
Solution for LC#2215: Find the Difference of Two Arrays
https://leetcode.com/problems/find-the-difference-of-two-arrays/
"""
import unittest


class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        set_num1 = set(nums1)
        set_num2 = set(nums2)
        return [list(set_num1 - set_num2), list(set_num2 - set_num1)]


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_example_1(self):
        nums1 = [1, 2, 3]
        nums2 = [2, 4, 6]
        self.assertEqual([[1, 3], [4, 6]], self.solution.findDifference(nums1, nums2))

    def test_example_2(self):
        nums1 = [1, 2, 3, 3]
        nums2 = [1, 1, 2, 2]
        self.assertEqual([[3], []], self.solution.findDifference(nums1, nums2))
