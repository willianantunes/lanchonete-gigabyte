"""
Solution for LC#387: First Unique Character in a String
https://leetcode.com/problems/first-unique-character-in-a-string/
"""
import unittest


class Solution:
    def firstUniqChar(self, s: str) -> int:
        database_of_chars = {}

        for index, char in enumerate(s):
            position, counter = database_of_chars.get(char, (index, 0))
            counter += 1
            database_of_chars[char] = (position, counter)

        for char in s:
            position, counter = database_of_chars[char]
            if counter == 1:
                return position

        return -1


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_example_1(self):
        s = "leetcode"
        self.assertEqual(0, self.solution.firstUniqChar(s))

    def test_example_2(self):
        s = "loveleetcode"
        self.assertEqual(2, self.solution.firstUniqChar(s))

    def test_example_3(self):
        s = "aabb"
        self.assertEqual(-1, self.solution.firstUniqChar(s))
