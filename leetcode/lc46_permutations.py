"""
Solution for LC#46: Permutations
https://leetcode.com/problems/permutations/
"""
import unittest


class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        length_of_numbers = len(nums)
        permutations = []

        if length_of_numbers == 1:
            permutations.append(nums)
            return permutations

        def _backtrack(remaining: int, candidates: list[int]):
            if remaining == 0:
                permutations.append(candidates.copy())
            else:
                for number in nums:
                    if number not in candidates:
                        candidates.append(number)
                        _backtrack(remaining - 1, candidates)
                        candidates.pop()

        _backtrack(length_of_numbers, [])
        return permutations


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_example_1(self):
        nums = [1, 2, 3]
        self.assertEqual(
            [
                [1, 2, 3],
                [1, 3, 2],
                [2, 1, 3],
                [2, 3, 1],
                [3, 1, 2],
                [3, 2, 1],
            ],
            self.solution.permute(nums),
        )

    def test_example_2(self):
        nums = [0, 1]
        self.assertEqual(
            [[0, 1], [1, 0]],
            self.solution.permute(nums),
        )

    def test_example_3(self):
        nums = [1]
        self.assertEqual([[1]], self.solution.permute(nums))
