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
        for number_of_interactions in range(number_of_colors):
            swapped = False
            end_index = number_of_colors - number_of_interactions - 1
            for left_pointer in range(0, end_index):
                right_pointer = left_pointer + 1
                left_value = nums[left_pointer]
                right_value = nums[right_pointer]
                if left_value > right_value:
                    nums[left_pointer], nums[right_pointer] = nums[right_pointer], nums[left_pointer]
                    swapped = True
            if not swapped:
                break


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
