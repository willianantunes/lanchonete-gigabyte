"""
Solution for LC#977: Squares of a Sorted Array
https://leetcode.com/problems/squares-of-a-sorted-array/
"""
import unittest


class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        queue = []
        copy_of_nums = nums.copy()
        number_of_nums = len(copy_of_nums)
        index = 0
        ordered_queue = []
        while index < number_of_nums:
            number = copy_of_nums[index]
            if number < 0:
                nums.pop(0)
                squared_number = number * number
                queue.append(squared_number)
                index += 1
            elif queue:
                lowest_number_from_queue = queue[-1]
                squared_number = number * number
                if squared_number < lowest_number_from_queue:
                    ordered_queue.append(squared_number)
                    index += 1
                else:
                    ordered_queue.append(queue.pop())
            else:
                ordered_queue.append(number * number)
                index += 1
        return ordered_queue + queue[::-1]


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
