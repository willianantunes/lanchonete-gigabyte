"""
Solution for LC#167: Two Sum II - Input Array Is Sorted
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
"""
import bisect
import unittest


def find_index(array: list, target: int):
    array_length = len(array)
    expected_index = bisect.bisect_left(array, target)
    if array_length > expected_index and array[expected_index] == target:
        return expected_index


class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        for index, value in enumerate(numbers):
            value_to_be_found = -1 * (value + (-1 * target))
            found_index = find_index(numbers, value_to_be_found)
            if found_index is not None and index != found_index:
                indexes = [index + 1, found_index + 1] if index < found_index else [found_index + 1, index + 1]
                return indexes


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
