"""
Solution for LC#258: Add Digits
https://leetcode.com/problems/add-digits/
"""
import unittest


class Solution:
    def addDigits(self, num: int) -> int:
        while len(num_in_str := str(num)) != 1:
            num = [int(digit) for digit in num_in_str]
            num = sum(num)
        return num


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(2, self.solution.addDigits(38))

    def test_example_2(self):
        self.assertEqual(0, self.solution.addDigits(0))
