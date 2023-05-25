"""
Solution for LC#189: Rotate Array
https://leetcode.com/problems/rotate-array/
"""
import unittest


class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        queue = []
        counter = 0
        while counter != k:
            while len(nums) > 1:
                queue.append(nums.pop(0))
            while queue:
                nums.append(queue.pop(0))
            counter += 1


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_example_1(self):
        nums = [1, 2, 3, 4, 5, 6, 7]
        k = 3
        self.solution.rotate(nums, k)
        self.assertEqual([5, 6, 7, 1, 2, 3, 4], nums)

    def test_example_2(self):
        nums = [-1, -100, 3, 99]
        k = 2
        self.solution.rotate(nums, k)
        self.assertEqual([3, 99, -1, -100], nums)
