"""
Solution for LC#567: Permutation in String
https://leetcode.com/problems/permutation-in-string/
"""
import unittest


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_as_array = sorted(s1)
        s1_length = len(s1)
        s2_length = len(s2)
        current_index = 0
        while current_index < s2_length:
            char = s2[current_index]
            if char in s1:
                window = s2[current_index : current_index + s1_length]
                sorted_window = sorted(window)
                if s1_as_array == sorted_window:
                    return True
            current_index += 1
        return False


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_example_1(self):
        s1 = "ab"
        s2 = "eidbaooo"
        self.assertEqual(True, self.solution.checkInclusion(s1, s2))

    def test_example_2(self):
        s1 = "ab"
        s2 = "eidboaoo"
        self.assertEqual(False, self.solution.checkInclusion(s1, s2))

    def test_example_3(self):
        s1 = "ab"
        s2 = "abcder"
        self.assertEqual(True, self.solution.checkInclusion(s1, s2))

    def test_example_4(self):
        s1 = "abc"
        s2 = "cabgh"
        self.assertEqual(True, self.solution.checkInclusion(s1, s2))

    def test_example_5(self):
        s1 = "abc"
        s2 = "ccccbbbbaaaa"
        self.assertEqual(False, self.solution.checkInclusion(s1, s2))

    def test_example_6(self):
        s1 = "abc"
        s2 = "cccbbbbaaaa"
        self.assertEqual(False, self.solution.checkInclusion(s1, s2))

    def test_example_7(self):
        s1 = "ccc"
        s2 = "cbac"
        self.assertEqual(False, self.solution.checkInclusion(s1, s2))

    def test_example_8(self):
        s1 = "adc"
        s2 = "dcda"
        self.assertEqual(True, self.solution.checkInclusion(s1, s2))
