"""
Solution for LC#136: Single Number
https://leetcode.com/problems/single-number/
"""
import unittest


class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        # https://www.geeksforgeeks.org/python-bitwise-operators/
        # https://en.wikipedia.org/wiki/Bitwise_operation
        xor = 0
        for num in nums:
            xor ^= num
        return xor


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_example_1(self):
        nums = [2, 2, 1]
        self.assertEqual(1, self.solution.singleNumber(nums))

    def test_example_2(self):
        nums = [4, 1, 2, 1, 2]
        self.assertEqual(4, self.solution.singleNumber(nums))

    def test_example_3(self):
        nums = [1]
        self.assertEqual(1, self.solution.singleNumber(nums))
