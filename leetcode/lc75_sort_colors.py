"""
Solution for LC#75: Sort Colors
https://leetcode.com/problems/sort-colors/
"""
import unittest


class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        number_of_colors = len(nums)
        bottom = middle = 0
        upper = number_of_colors - 1
        while middle <= upper:
            middle_value = nums[middle]
            if middle_value == 1:
                middle += 1
            elif middle_value == 0:
                nums[bottom], nums[middle] = nums[middle], nums[bottom]
                middle += 1
                bottom += 1
            else:
                nums[middle], nums[upper] = nums[upper], nums[middle]
                upper -= 1


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_example_1(self):
        nums = [2, 0, 2, 1, 1, 0]
        self.solution.sortColors(nums)
        expected = [0, 0, 1, 1, 2, 2]
        self.assertEqual(expected, nums)

    def test_example_2(self):
        nums = [2, 0, 1]
        self.solution.sortColors(nums)
        expected = [0, 1, 2]
        self.assertEqual(expected, nums)

    def test_example_3(self):
        nums = [0, 2, 1]
        self.solution.sortColors(nums)
        expected = [0, 1, 2]
        self.assertEqual(expected, nums)
