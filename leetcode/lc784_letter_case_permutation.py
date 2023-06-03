"""
Solution for LC#784: Letter Case Permutation
https://leetcode.com/problems/letter-case-permutation/
"""
import unittest


class Solution:
    def letterCasePermutation(self, s: str) -> list[str]:
        letters_positions = []
        for index, char in enumerate(s):
            if not char.isdigit():
                letters_positions.append(index)
        if not letters_positions:
            return [s]

        permutations = []

        def _backtrack(remaining: int, candidate: list[str], start_index: int):
            if remaining == 0:
                permutations.append("".join(candidate))
            else:
                for target_index in range(start_index, len(letters_positions)):
                    index = letters_positions[target_index]
                    candidate[index] = candidate[index].lower()
                    _backtrack(remaining - 1, candidate, target_index + 1)
                    candidate[index] = candidate[index].upper()
                    _backtrack(remaining - 1, candidate, target_index + 1)
                    candidate = list(s)

        _backtrack(len(letters_positions), list(s), 0)
        return permutations


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_example_1(self):
        s = "a1b2"
        self.assertEqual(["a1b2", "a1B2", "A1b2", "A1B2"], self.solution.letterCasePermutation(s))

    def test_example_2(self):
        s = "3z4"
        self.assertEqual(["3z4", "3Z4"], self.solution.letterCasePermutation(s))

    def test_example_3(self):
        s = "34"
        self.assertEqual(["34"], self.solution.letterCasePermutation(s))
