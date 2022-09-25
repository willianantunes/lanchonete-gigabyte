"""
Solution for LC#15: 3Sum
https://leetcode.com/problems/3sum/
"""
import unittest


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        target = 0
        nums.sort()
        nums_length = len(nums)

        result = []
        for i in range(nums_length):
            i_value = nums[i]

            is_it_impossible_to_reach_target = i_value > target
            if is_it_impossible_to_reach_target:
                break

            i_adjacent_element = nums[i - 1]
            skip_to_avoid_duplicate_entries_regarding_i = i > 0 and i_value == i_adjacent_element
            if skip_to_avoid_duplicate_entries_regarding_i:
                continue

            left_pointer = i + 1
            right_pointer = nums_length - 1
            while left_pointer < right_pointer:
                left_value, right_value = nums[left_pointer], nums[right_pointer]
                total = i_value + left_value + right_value
                if total > target:
                    right_pointer -= 1
                elif total < target:
                    left_pointer += 1
                else:
                    result.append([i_value, left_value, right_value])
                    left_pointer += 1
                    right_pointer -= 1

                    def skip_to_avoid_duplicate_entries_regarding_left():
                        return left_pointer < right_pointer and nums[left_pointer] == nums[left_pointer - 1]

                    def skip_to_avoid_duplicate_entries_regarding_right():
                        return left_pointer < right_pointer and nums[right_pointer] == nums[right_pointer + 1]

                    while skip_to_avoid_duplicate_entries_regarding_left():
                        left_pointer += 1
                    while skip_to_avoid_duplicate_entries_regarding_right():
                        right_pointer -= 1

        return result


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_example_1(self):
        nums = [-1, 0, 1, 2, -1, -4]
        self.assertEqual([[-1, -1, 2], [-1, 0, 1]], self.solution.threeSum(nums))

    def test_example_2(self):
        nums = [0, 1, 1]
        self.assertEqual([], self.solution.threeSum(nums))

    def test_example_3(self):
        nums = [0, 0, 0]
        self.assertEqual([[0, 0, 0]], self.solution.threeSum(nums))

    def test_example_4(self):
        nums = [3, -2, 1, 0]
        self.assertEqual([], self.solution.threeSum(nums))

    def test_example_5(self):
        nums = [-1, 0, 1, 2, -1, -4, -2, -3, 3, 0, 4]
        self.assertEqual(
            [
                [-4, 0, 4],
                [-4, 1, 3],
                [-3, -1, 4],
                [-3, 0, 3],
                [-3, 1, 2],
                [-2, -1, 3],
                [-2, 0, 2],
                [-1, -1, 2],
                [-1, 0, 1],
            ],
            self.solution.threeSum(nums),
        )

    def test_example_6(self):
        nums = [-2, 0, 1, 1, 2]
        self.assertEqual([[-2, 0, 2], [-2, 1, 1]], self.solution.threeSum(nums))
