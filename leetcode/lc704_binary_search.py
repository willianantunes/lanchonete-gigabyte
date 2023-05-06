"""
Solution for LC#704: Binary Search
https://leetcode.com/problems/binary-search/
"""
import unittest


class Solution:
    def search(self, nums: list[int], target: int) -> int:
        numbers_count = len(nums)
        pointer_right, pointer_left = 0, numbers_count - 1
        while pointer_right <= pointer_left:
            middle_index = (pointer_left + pointer_right) // 2
            middle_value = nums[middle_index]
            if middle_value == target:
                return middle_index
            elif target < middle_value:
                pointer_left = middle_index - 1
            else:
                pointer_right = middle_index + 1
        return -1


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_example_1(self):
        nums = [-1, 0, 3, 5, 9, 12]
        target = 9
        self.assertEqual(4, self.solution.search(nums, target))

    def test_example_2(self):
        nums = [-1, 0, 3, 5, 9, 12]
        target = 2
        self.assertEqual(-1, self.solution.search(nums, target))
