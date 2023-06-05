"""
Solution for LC#136: Single Number
https://leetcode.com/problems/single-number/
"""
import unittest


class Solution:
    def hammingWeight(self, n: int) -> int:
        counter = 0
        while n:
            print(f"Current N: {n:08b}")
            n &= n - 1
            counter += 1
        return counter


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_example_1(self):
        n = int("1011", 2)
        self.assertEqual(3, self.solution.hammingWeight(n))

    def test_example_2(self):
        n = int("10000000", 2)
        self.assertEqual(1, self.solution.hammingWeight(n))

    def test_example_3(self):
        n = int("11111111111111111111111111111101", 2)
        self.assertEqual(31, self.solution.hammingWeight(n))
