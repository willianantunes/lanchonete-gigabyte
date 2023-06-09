"""
Solution for LC#744: Find Smallest Letter Greater Than Target
https://leetcode.com/problems/find-smallest-letter-greater-than-target/
"""
import unittest


class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        target_code = ord(target)
        number_of_letters = len(letters)
        standard_output_if_no_match = letters[0]

        def _find_greatest_letter(index: int) -> str:
            if index >= number_of_letters:
                return standard_output_if_no_match
            current_letter = letters[index]
            current_letter_code = ord(current_letter)
            next_letter = letters[index + 1] if index + 1 < number_of_letters else None
            next_letter_code = ord(next_letter) if next_letter else None
            if current_letter_code <= target_code and next_letter and next_letter_code > target_code:
                return next_letter

            return _find_greatest_letter(index + 1)

        return _find_greatest_letter(0)


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_example_1(self):
        letters = ["c", "f", "j"]
        target = "a"
        self.assertEqual("c", self.solution.nextGreatestLetter(letters, target))

    def test_example_2(self):
        letters = ["c", "f", "j"]
        target = "c"
        self.assertEqual("f", self.solution.nextGreatestLetter(letters, target))

    def test_example_3(self):
        letters = ["x", "x", "y", "y"]
        target = "z"
        self.assertEqual("x", self.solution.nextGreatestLetter(letters, target))

    def test_example_4(self):
        letters = ["a", "z"]
        target = "y"
        self.assertEqual("z", self.solution.nextGreatestLetter(letters, target))

    def test_example_5(self):
        letters = ["c", "f", "j"]
        target = "j"
        self.assertEqual("c", self.solution.nextGreatestLetter(letters, target))

    def test_example_6(self):
        letters = ["e", "e", "g", "g"]
        target = "g"
        self.assertEqual("e", self.solution.nextGreatestLetter(letters, target))
