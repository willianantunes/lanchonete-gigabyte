"""
Solution for LC#217: Contains Duplicate
https://leetcode.com/problems/contains-duplicate/
"""
import unittest

from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        counter_entries: dict[int, int] = {}
        for value in nums:
            counter = counter_entries.get(value, 0) + 1
            counter_entries[value] = counter
            if counter > 1:
                return True
        return False


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_example_1(self):
        nums = [1, 2, 3, 1]
        self.assertTrue(self.solution.containsDuplicate(nums))

    def test_example_2(self):
        nums = [1, 2, 3, 4]
        self.assertFalse(self.solution.containsDuplicate(nums))

    def test_example_3(self):
        nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
        self.assertTrue(self.solution.containsDuplicate(nums))
