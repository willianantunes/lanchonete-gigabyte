"""
Solution for LC#242: Valid Anagram
https://leetcode.com/problems/valid-anagram/
"""
import unittest


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        database_from_s = {}
        database_from_t = {}

        for char in s:
            counter = database_from_s.get(char, 0) + 1
            database_from_s[char] = counter

        for char in t:
            counter = database_from_t.get(char, 0) + 1
            database_from_t[char] = counter

        return database_from_s == database_from_t


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_example_1(self):
        s = "anagram"
        t = "nagaram"
        self.assertEqual(True, self.solution.isAnagram(s, t))

    def test_example_2(self):
        s = "rat"
        t = "car"
        self.assertEqual(False, self.solution.isAnagram(s, t))
