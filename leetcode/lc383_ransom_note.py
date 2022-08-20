"""
Solution for LC#383: Ransom Note
https://leetcode.com/problems/ransom-note/
"""
import unittest


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        storage_letters_must_be_present = {}
        for char in ransomNote:
            counter = storage_letters_must_be_present.get(char, 0) + 1
            storage_letters_must_be_present[char] = counter

        storage_letters_magazine = {}
        for char in magazine:
            counter = storage_letters_magazine.get(char, 0) + 1
            storage_letters_magazine[char] = counter

        for key in storage_letters_must_be_present.keys():
            magazine_char_counter = storage_letters_magazine.get(key)
            if not magazine_char_counter:
                return False
            char_present_counter = storage_letters_must_be_present[key]
            if magazine_char_counter < char_present_counter:
                return False

        return True


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_example_1(self):
        ransomNote = "a"
        magazine = "b"
        self.assertEqual(False, self.solution.canConstruct(ransomNote, magazine))

    def test_example_2(self):
        ransomNote = "aa"
        magazine = "ab"
        self.assertEqual(False, self.solution.canConstruct(ransomNote, magazine))

    def test_example_3(self):
        ransomNote = "aa"
        magazine = "aab"
        self.assertEqual(True, self.solution.canConstruct(ransomNote, magazine))

    def test_example_4(self):
        ransomNote = "bg"
        magazine = "efjbdfbdgfjhhaiigfhbaejahgfbbgbjagbddfgdiaigdadhcfcj"
        self.assertEqual(True, self.solution.canConstruct(ransomNote, magazine))
