"""
Solution for LC#136: Single Number
https://leetcode.com/problems/single-number/
"""
import unittest


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        return n & (n - 1) == 0


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_example_1(self):
        n = 1
        self.assertEqual(True, self.solution.isPowerOfTwo(n))

    def test_example_2(self):
        n = 16
        self.assertEqual(True, self.solution.isPowerOfTwo(n))

    def test_example_3(self):
        n = 3
        self.assertEqual(False, self.solution.isPowerOfTwo(n))
