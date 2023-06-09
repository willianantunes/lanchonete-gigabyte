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
        number_of_nums = len(nums)
        pointer_left, pointer_right = 0, 1

        while pointer_left <= pointer_right < number_of_nums:
            pointer_left_value = nums[pointer_left]
            pointer_right_value = nums[pointer_right]
            if pointer_left_value == 0 and pointer_right_value != 0:
                nums[pointer_left], nums[pointer_right] = nums[pointer_right], nums[pointer_left]
                pointer_left += 1
                pointer_right += 1
            elif pointer_left_value == 0 and pointer_right_value == 0:
                pointer_right += 1
            elif pointer_left_value != 0 and pointer_right_value == 0:
                pointer_left += 1
                pointer_right += 1
            else:
                pointer_left += 2
                pointer_right += 2


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
