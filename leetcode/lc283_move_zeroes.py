"""
Solution for LC#283: Move Zeroes
https://leetcode.com/problems/move-zeroes/
"""
import unittest


class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums_length = len(nums)

        pointer_swap = 0
        pointer_comparator = 1

        while pointer_comparator < nums_length and pointer_swap < nums_length:
            if nums[pointer_swap] != 0:
                pointer_swap += 1
                continue
            if pointer_comparator < pointer_swap:
                pointer_comparator = pointer_swap
            if nums[pointer_comparator] == 0:
                pointer_comparator += 1
            elif pointer_comparator < nums_length and pointer_swap < nums_length:
                if nums[pointer_swap] == 0:
                    nums[pointer_swap], nums[pointer_comparator] = nums[pointer_comparator], nums[pointer_swap]


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_example_1(self):
        nums = [0, 1, 0, 3, 12]
        self.solution.moveZeroes(nums)
        self.assertEqual([1, 3, 12, 0, 0], nums)

    def test_example_2(self):
        nums = [0]
        self.solution.moveZeroes(nums)
        self.assertEqual([0], nums)

    def test_example_3(self):
        nums = [0, 1, 0, 0]
        self.solution.moveZeroes(nums)
        self.assertEqual([1, 0, 0, 0], nums)

    def test_example_4(self):
        nums = [0, 1]
        self.solution.moveZeroes(nums)
        self.assertEqual([1, 0], nums)

    def test_example_5(self):
        nums = [2, 1]
        self.solution.moveZeroes(nums)
        self.assertEqual([2, 1], nums)

    def test_example_6(self):
        nums = [1, 2, 3, 1]
        self.solution.moveZeroes(nums)
        self.assertEqual([1, 2, 3, 1], nums)

    def test_example_7(self):
        nums = [4, 2, 4, 0, 0, 3, 0, 5, 1, 0]
        self.solution.moveZeroes(nums)
        self.assertEqual([4, 2, 4, 3, 5, 1, 0, 0, 0, 0], nums)
