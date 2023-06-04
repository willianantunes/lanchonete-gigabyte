"""
Solution for LC#198: House Robber
https://leetcode.com/problems/house-robber/
"""
import unittest


class Solution:
    def rob(self, nums: list[int]) -> int:
        cache = {}

        def _rob(target_house: int):
            if target_house < 0:
                return 0
            if target_house in cache:
                return cache[target_house]

            house_target_minus_two = _rob(target_house - 2)
            current_house = nums[target_house]
            house_target_minus_one = _rob(target_house - 1)
            loot = max(house_target_minus_two + current_house, house_target_minus_one)
            cache[target_house] = loot
            return loot

        return _rob(len(nums) - 1)


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_example_1(self):
        nums = [1, 2, 3, 1]
        self.assertEqual(4, self.solution.rob(nums))

    def test_example_2(self):
        nums = [2, 7, 9, 3, 1]
        self.assertEqual(12, self.solution.rob(nums))

    def test_example_3(self):
        nums = [2, 1, 1, 2]
        self.assertEqual(4, self.solution.rob(nums))

    def test_example_4(self):
        nums = [
            183,
            219,
            57,
            193,
            94,
            233,
            202,
            154,
            65,
            240,
            97,
            234,
            100,
            249,
            186,
            66,
            90,
            238,
            168,
            128,
            177,
            235,
            50,
            81,
            185,
            165,
            217,
            207,
            88,
            80,
            112,
            78,
            135,
            62,
            228,
            247,
            211,
        ]
        self.assertEqual(3365, self.solution.rob(nums))

    def test_example_5(self):
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        self.assertEqual(64, self.solution.rob(nums))

    def test_example_6(self):
        nums = [15, 5, 20, 40, 2, 6, 9]
        self.assertEqual(64, self.solution.rob(nums))
