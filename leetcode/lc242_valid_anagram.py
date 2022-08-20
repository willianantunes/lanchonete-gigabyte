"""
Solution for LC#242: Valid Anagram
https://leetcode.com/problems/valid-anagram/
"""
import unittest


def quick_sort(array: list):
    array_length = len(array)
    less_than_pivot = []
    greater_than_pivot = []
    equal_pivot = []

    if array_length > 1:
        pivot = array[0]
        for entry in array:
            if entry > pivot:
                greater_than_pivot.append(entry)
            elif entry < pivot:
                less_than_pivot.append(entry)
            else:
                equal_pivot.append(entry)
        return quick_sort(less_than_pivot) + equal_pivot + quick_sort(greater_than_pivot)
    else:
        return array


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_codes = []
        for char in s:
            char_as_code = ord(char)
            s_codes.append(char_as_code)

        t_codes = []
        for char in t:
            char_as_code = ord(char)
            t_codes.append(char_as_code)

        s_codes = quick_sort(s_codes)
        t_codes = quick_sort(t_codes)

        return s_codes == t_codes


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
