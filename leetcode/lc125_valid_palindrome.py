"""
Solution for LC#125: Valid Palindrome
https://leetcode.com/problems/valid-palindrome/
Two Pointers / String
"""
import unittest


class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        s = s.lower()

        def _valid_char(value: str):
            first_condition = ord("a") <= ord(value) <= ord("z")
            second_condition = ord("A") <= ord(value) <= ord("Z")
            third_condition = ord("0") <= ord(value) <= ord("9")
            if first_condition or second_condition or third_condition:
                return True
            return False

        while left != right and left < right:
            char_left = s[left]
            char_left_is_valid = _valid_char(char_left)
            if not char_left_is_valid:
                left += 1
                continue
            char_right = s[right]
            char_right_is_valid = _valid_char(char_right)
            if not char_right_is_valid:
                right -= 1
                continue
            if char_right != char_left:
                return False
            left += 1
            right -= 1

        return True


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_example_1(self):
        s = "A man, a plan, a canal: Panama"
        self.assertEqual(True, self.solution.isPalindrome(s))

    def test_example_2(self):
        s = "race a car"
        self.assertEqual(False, self.solution.isPalindrome(s))

    def test_example_3(self):
        s = " "
        self.assertEqual(True, self.solution.isPalindrome(s))

    def test_example_4(self):
        s = "0P"
        self.assertEqual(False, self.solution.isPalindrome(s))
