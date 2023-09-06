"""
Solution for LC#128. Longest Consecutive Sequence
https://leetcode.com/problems/longest-consecutive-sequence/
"""
import unittest


class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        longest_sequence_size = 0
        nums_set = set(nums)

        for num in nums:
            num_before = num - 1
            if num_before not in nums_set:
                counter = 0
                while (counter + num) in nums_set:
                    counter += 1
                longest_sequence_size = max(longest_sequence_size, counter)

        return longest_sequence_size


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_example_1(self):
        nums = [100, 4, 200, 1, 3, 2]
        self.assertEqual(self.solution.longestConsecutive(nums), 4)

    def test_example_2(self):
        nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
        self.assertEqual(9, self.solution.longestConsecutive(nums))
