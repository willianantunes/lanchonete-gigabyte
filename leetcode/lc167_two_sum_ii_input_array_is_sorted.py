"""
Solution for LC#167: Two Sum II - Input Array Is Sorted
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
"""
import unittest


class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        numbers_length = len(numbers)
        if numbers_length == 2:
            return [1, 2]

        left_pointer = 0
        right_pointer = numbers_length - 1
        while left_pointer < right_pointer:
            left_value = numbers[left_pointer]
            right_value = numbers[right_pointer]
            total = left_value + right_value
            if total < target:
                left_pointer += 1
            elif total > target:
                right_pointer -= 1
            else:
                return [left_pointer + 1, right_pointer + 1]


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_example_1(self):
        numbers = [2, 7, 11, 15]
        target = 9
        self.assertEqual([1, 2], self.solution.twoSum(numbers, target))

    def test_example_2(self):
        numbers = [2, 3, 4]
        target = 6
        self.assertEqual([1, 3], self.solution.twoSum(numbers, target))

    def test_example_3(self):
        numbers = [-1, 0]
        target = -1
        self.assertEqual([1, 2], self.solution.twoSum(numbers, target))
