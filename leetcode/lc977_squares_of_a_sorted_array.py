"""
Solution for LC#977: Squares of a Sorted Array
https://leetcode.com/problems/squares-of-a-sorted-array/
"""
import unittest


class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        number_of_nums = len(nums)
        new_array = [0] * number_of_nums
        pointer_left, pointer_right = 0, number_of_nums - 1
        insert_position = number_of_nums - 1

        while insert_position >= 0:
            pointer_left_value = nums[pointer_left] ** 2
            pointer_right_value = nums[pointer_right] ** 2
            if pointer_left_value < pointer_right_value:
                new_array[insert_position] = pointer_right_value
                pointer_right -= 1
            else:
                new_array[insert_position] = pointer_left_value
                pointer_left += 1
            insert_position -= 1

        return new_array


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_example_1(self):
        nums = [-4, -1, 0, 3, 10]
        self.assertEqual([0, 1, 9, 16, 100], self.solution.sortedSquares(nums))

    def test_example_2(self):
        nums = [-7, -3, 2, 3, 11]
        self.assertEqual([4, 9, 9, 49, 121], self.solution.sortedSquares(nums))

    def test_example_3(self):
        nums = [-5, -3, -2, -1]
        self.assertEqual([1, 4, 9, 25], self.solution.sortedSquares(nums))
