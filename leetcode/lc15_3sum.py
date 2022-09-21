"""
Solution for LC#15: 3Sum
https://leetcode.com/problems/3sum/
"""
import unittest


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        database = {}
        nums_length = len(nums)

        for i in range(nums_length):
            for k in range(nums_length):
                if i == k:
                    continue
                for j in {*range(i + 1, k), *range(k + i + 1, nums_length)}:
                    first_criteria = i != j and i != k and j != k
                    second_criteria = nums[i] + nums[j] + nums[k] == 0
                    if first_criteria and second_criteria:
                        keys = [i, j, k]
                        keys.sort()
                        index = "".join([str(key) for key in keys])
                        triplet_key = [nums[i], nums[j], nums[k]]
                        triplet_key.sort()
                        database[index] = triplet_key, "".join([str(key) for key in triplet_key])

        result = {}
        for triplet_key, triplet_hash in database.values():
            result[triplet_hash] = triplet_key

        return list(result.values())


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_example_1(self):
        nums = [-1, 0, 1, 2, -1, -4]
        self.assertEqual([[-1, 0, 1], [-1, -1, 2]], self.solution.threeSum(nums))

    def test_example_2(self):
        nums = [0, 1, 1]
        self.assertEqual([], self.solution.threeSum(nums))

    def test_example_3(self):
        nums = [0, 0, 0]
        self.assertEqual([[0, 0, 0]], self.solution.threeSum(nums))

    def test_example_4(self):
        # fmt: off
        nums = [-9,14,-7,-8,9,1,-10,-8,13,12,6,9,3,-3,-15,-15,1,8,-7,-4,-6,8,2,-10,8,11,-15,3,0,-11,-1,-1,10,0,6,5,-14,3,12,-15,-7,-5,9,11,-1,1,3,-15,-5,11,-12,-4,-4,-2,-6,-10,-6,-6,0,2,-9,14,-14,-14,-9,-1,-2,-7,-12,-13,-15,-4,-3,1,14,3,-12,3,3,-10,-9,-1,-7,3,12,-6,0,13,4,-15,0,2,6,1,3,13,8,-13,13,11,11,13,14,-6]
        # fmt: on
        self.assertEqual(
            [
                [-9, -5, 14],
                [-9, 0, 9],
                [-9, 1, 8],
                [-9, -4, 13],
                [-9, -3, 12],
                [-9, 3, 6],
                [-9, -2, 11],
                [-9, -1, 10],
                [-9, 4, 5],
                [-7, -7, 14],
                [-8, -6, 14],
                [-15, 1, 14],
                [-10, -4, 14],
                [-11, -3, 14],
                [-14, 0, 14],
                [-13, -1, 14],
                [-12, -2, 14],
                [-7, -2, 9],
                [-7, 1, 6],
                [-7, -6, 13],
                [-7, -5, 12],
                [-7, 3, 4],
                [-7, -3, 10],
                [-7, -1, 8],
                [-7, -4, 11],
                [-7, 2, 5],
                [-8, -1, 9],
                [-8, -5, 13],
                [-8, -4, 12],
                [-8, 2, 6],
                [-8, 3, 5],
                [-8, -3, 11],
                [-8, 0, 8],
                [-8, -2, 10],
                [-10, 1, 9],
                [-15, 6, 9],
                [-12, 3, 9],
                [-6, -3, 9],
                [-5, -4, 9],
                [-11, 2, 9],
                [-14, 5, 9],
                [-13, 4, 9],
                [-14, 1, 13],
                [-13, 1, 12],
                [-4, 1, 3],
                [-3, 1, 2],
                [-2, 1, 1],
                [-6, 1, 5],
                [-12, 1, 11],
                [-1, 0, 1],
                [-11, 1, 10],
                [-5, 1, 4],
                [-10, -3, 13],
                [-10, -2, 12],
                [-10, 4, 6],
                [-10, 2, 8],
                [-10, -1, 11],
                [-10, 0, 10],
                [-15, 2, 13],
                [-13, 0, 13],
                [-11, -2, 13],
                [-12, -1, 13],
                [-15, 3, 12],
                [-6, -6, 12],
                [-14, 2, 12],
                [-12, 0, 12],
                [-11, -1, 12],
                [-3, -3, 6],
                [-14, 6, 8],
                [-4, -2, 6],
                [-6, 0, 6],
                [-11, 5, 6],
                [-5, -1, 6],
                [-12, 6, 6],
                [-3, 0, 3],
                [-11, 3, 8],
                [-6, 3, 3],
                [-5, 2, 3],
                [-14, 3, 11],
                [-2, -1, 3],
                [-13, 3, 10],
                [-5, -3, 8],
                [-3, -1, 4],
                [-3, -2, 5],
                [-15, 4, 11],
                [-15, 5, 10],
                [-4, -4, 8],
                [-6, -2, 8],
                [-13, 5, 8],
                [-12, 4, 8],
                [-6, -4, 10],
                [-4, 2, 2],
                [-4, 0, 4],
                [-4, -1, 5],
                [-6, 2, 4],
                [-6, -5, 11],
                [-13, 2, 11],
                [-2, 0, 2],
                [-1, -1, 2],
                [-12, 2, 10],
                [-11, 0, 11],
                [0, 0, 0],
                [-5, 0, 5],
                [-14, 4, 10],
                [-5, -5, 10],
                [-2, -2, 4],
            ],
            self.solution.threeSum(nums),
        )

    def test_example_5(self):
        nums = [3, -2, 1, 0]
        self.assertEqual([], self.solution.threeSum(nums))

    def test_example_6(self):
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
