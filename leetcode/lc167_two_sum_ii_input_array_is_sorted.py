"""
Solution for LC#167: Two Sum II - Input Array Is Sorted
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
"""
import unittest


class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        pointer_left, pointer_right = 0, len(numbers) - 1
        while pointer_left <= pointer_right:
            sum_from_each_pointer_value = numbers[pointer_left] + numbers[pointer_right]
            if sum_from_each_pointer_value < target:
                pointer_left += 1
            elif sum_from_each_pointer_value > target:
                pointer_right -= 1
            else:
                return [pointer_left + 1, pointer_right + 1]


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

    def test_example_4(self):
        numbers = [0, 0, 3, 4]
        target = 0
        self.assertEqual([1, 2], self.solution.twoSum(numbers, target))

    def test_example_5(self):
        numbers = [5, 25, 75]
        target = 100
        self.assertEqual([2, 3], self.solution.twoSum(numbers, target))

    def test_example_6(self):
        numbers = [3, 24, 50, 79, 88, 150, 345]
        target = 200
        self.assertEqual([3, 6], self.solution.twoSum(numbers, target))
