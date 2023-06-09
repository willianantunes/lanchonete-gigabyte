"""
Solution for LC#557: Reverse Words in a String III
https://leetcode.com/problems/reverse-words-in-a-string-iii/
"""
import unittest


class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(" ")
        inverted_words = []
        for w in words:
            w_as_list = list(w)
            pointer_left, pointer_right = 0, len(w_as_list) - 1
            while pointer_left <= pointer_right:
                w_as_list[pointer_left], w_as_list[pointer_right] = (w_as_list[pointer_right], w_as_list[pointer_left])
                pointer_left += 1
                pointer_right -= 1
            inverted_words.append("".join(w_as_list))

        return " ".join(inverted_words)


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_example_1(self):
        s = "Let's take LeetCode contest"
        self.assertEqual("s'teL ekat edoCteeL tsetnoc", self.solution.reverseWords(s))

    def test_example_2(self):
        s = "God Ding"
        self.assertEqual("doG gniD", self.solution.reverseWords(s))
