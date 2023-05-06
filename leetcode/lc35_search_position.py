"""
Solution for LC#35: Search Insert Position
https://leetcode.com/problems/search-insert-position/
"""
import unittest


class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        number_of_nums = len(nums)
        pointer_left, pointer_right = 0, number_of_nums - 1
        while pointer_left <= pointer_right:
            middle_index = pointer_left + (pointer_right - pointer_left) // 2
            middle_value = nums[middle_index]
            if middle_value == target:
                return middle_index
            elif target < middle_value:
                pointer_right = middle_index - 1
            else:
                pointer_left = middle_index + 1
        return pointer_left


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_example_1(self):
        nums = [1, 3, 5, 6]
        target = 5
        self.assertEqual(2, self.solution.searchInsert(nums, target))

    def test_example_2(self):
        nums = [1, 3, 5, 6]
        target = 2
        self.assertEqual(1, self.solution.searchInsert(nums, target))

    def test_example_3(self):
        nums = [1, 3, 5, 6]
        target = 7
        self.assertEqual(4, self.solution.searchInsert(nums, target))
