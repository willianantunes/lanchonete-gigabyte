"""
Solution for LC#3: Longest Substring Without Repeating Characters
https://leetcode.com/problems/longest-substring-without-repeating-characters/
"""
import bisect
import unittest


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        database = {}
        longest_substring = 0
        index = 0
        position = 1
        while index < len(s):
            char = s[index]
            counter = database.get(char, 0) + 1
            if counter == 1:
                database[char] = counter
                index += 1
            else:
                number_of_chars = len(database)
                longest_substring = max(longest_substring, number_of_chars)
                database = {}
                index = position
                position += 1

        number_of_chars = len(database)
        longest_substring = max(longest_substring, number_of_chars)
        return longest_substring


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_example_1(self):
        s = "abcabcbb"
        self.assertEqual(3, self.solution.lengthOfLongestSubstring(s))

    def test_example_2(self):
        s = "bbbbb"
        self.assertEqual(1, self.solution.lengthOfLongestSubstring(s))

    def test_example_3(self):
        s = "pwwkew"
        self.assertEqual(3, self.solution.lengthOfLongestSubstring(s))

    def test_example_4(self):
        s = "abcabcdb"
        self.assertEqual(4, self.solution.lengthOfLongestSubstring(s))

    def test_example_5(self):
        s = "abcabcde"
        self.assertEqual(5, self.solution.lengthOfLongestSubstring(s))

    def test_example_6(self):
        s = "dvdf"
        self.assertEqual(3, self.solution.lengthOfLongestSubstring(s))
