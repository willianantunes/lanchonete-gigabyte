"""
Solution for LC#557: Reverse Words in a String III
https://leetcode.com/problems/reverse-words-in-a-string-iii/
"""
import unittest


class Solution:
    def reverseWords(self, s: str) -> str:
        def _invert_word(word: str):
            word_as_list = list(word)
            pointer_left = 0
            pointer_right = len(word_as_list) - 1
            while pointer_left < pointer_right:
                word_as_list[pointer_left], word_as_list[pointer_right] = (
                    word_as_list[pointer_right],
                    word_as_list[pointer_left],
                )
                pointer_left += 1
                pointer_right -= 1
            return "".join(word_as_list)

        words = s.split(" ")
        reversed_words = []
        for word in words:
            reversed_word = _invert_word(word)
            reversed_words.append(reversed_word)

        return " ".join(reversed_words)


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_example_1(self):
        s = "Let's take LeetCode contest"
        self.assertEqual("s'teL ekat edoCteeL tsetnoc", self.solution.reverseWords(s))

    def test_example_2(self):
        s = "God Ding"
        self.assertEqual("doG gniD", self.solution.reverseWords(s))
