"""
Solution for LC#344: Reverse String
https://leetcode.com/problems/reverse-string/
"""
import unittest


class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        pointer_left = 0
        pointer_right = len(s) - 1
        while pointer_left < pointer_right:
            s[pointer_left], s[pointer_right] = s[pointer_right], s[pointer_left]
            pointer_left += 1
            pointer_right -= 1


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_example_1(self):
        s = ["h", "e", "l", "l", "o"]
        self.solution.reverseString(s)
        self.assertEqual(["o", "l", "l", "e", "h"], s)

    def test_example_2(self):
        s = ["H", "a", "n", "n", "a", "h"]
        self.solution.reverseString(s)
        self.assertEqual(["h", "a", "n", "n", "a", "H"], s)
