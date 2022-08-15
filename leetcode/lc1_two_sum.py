"""
Solution for LC#1: Two Sum
https://leetcode.com/problems/two-sum/
"""
import unittest


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        number_of_entries = len(nums)
        if number_of_entries == 2:
            return [0, 1]

        for left_pointer, value in enumerate(nums):
            right_pointer = left_pointer + 1
            while right_pointer < number_of_entries:
                current_sum = value + nums[right_pointer]
                if current_sum == target:
                    return [left_pointer, right_pointer]
                right_pointer += 1


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_example_1(self):
        nums = [2, 7, 11, 15]
        target = 9
        self.assertEqual([0, 1], self.solution.twoSum(nums, target))

    def test_example_2(self):
        nums = [3, 2, 4]
        target = 6
        self.assertEqual([1, 2], self.solution.twoSum(nums, target))

    def test_example_3(self):
        nums = [3, 3]
        target = 6
        self.assertEqual([0, 1], self.solution.twoSum(nums, target))
