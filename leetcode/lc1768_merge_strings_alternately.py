"""
Solution for LC#1768: Merge Strings Alternately
https://leetcode.com/problems/merge-strings-alternately/
"""
import unittest


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word1_length = len(word1)
        word2_length = len(word2)
        database_word1 = {}
        database_word2 = {}
        for index, value in enumerate(word1):
            database_word1[index] = value
        for index, value in enumerate(word2):
            database_word2[index] = value
        highest_value = word1_length if word1_length > word2_length else word2_length
        merged = []
        for index in range(highest_value):
            value_1 = database_word1.get(index)
            if value_1:
                merged.append(value_1)
            value_2 = database_word2.get(index)
            if value_2:
                merged.append(value_2)
        return "".join(merged)


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_example_1(self):
        word1 = "ab"
        word2 = "pqrs"
        self.assertEqual("apbqrs", self.solution.mergeAlternately(word1, word2))

    def test_example_2(self):
        word1 = "abcd"
        word2 = "pq"
        self.assertEqual("apbqcd", self.solution.mergeAlternately(word1, word2))
