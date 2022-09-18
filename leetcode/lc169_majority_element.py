"""
Solution for LC#169: Majority Element
https://leetcode.com/problems/majority-element/
"""
import unittest


class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        database = {}
        majority_count = len(nums) // 2

        for value in nums:
            counter = database.get(value, 0) + 1
            database[value] = counter
            if counter > majority_count:
                return value


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_example_1(self):
        nums = [3, 2, 3]
        self.assertEqual(3, self.solution.majorityElement(nums))

    def test_example_2(self):
        nums = [2, 2, 1, 1, 1, 2, 2]
        self.assertEqual(2, self.solution.majorityElement(nums))
