"""
Solution for LC#20: Valid Parentheses
https://leetcode.com/problems/valid-parentheses/
"""
import unittest


class Solution:
    def isValid(self, s: str) -> bool:
        is_even = len(s) % 2 == 0
        if not is_even:
            return False

        open_and_close_values = {
            "{": "}",
            "(": ")",
            "[": "]",
        }
        stack = []

        for char in s:
            if char in open_and_close_values:
                stack.append(char)
            else:
                last_appended_value = stack.pop() if stack else None
                if not last_appended_value:
                    return False
                expected_value_to_close = open_and_close_values[last_appended_value]
                if char != expected_value_to_close:
                    return False

        return len(stack) == 0


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_example_0(self):
        s = "()"
        self.assertEqual(True, self.solution.isValid(s))

    def test_example_1(self):
        s = "()[]{}"
        self.assertEqual(True, self.solution.isValid(s))

    def test_example_2(self):
        s = "(]"
        self.assertEqual(False, self.solution.isValid(s))

    def test_example_3(self):
        s = "([)]"
        self.assertEqual(False, self.solution.isValid(s))

    def test_example_4(self):
        s = "{{}[][[[]]]}"
        self.assertEqual(True, self.solution.isValid(s))

    def test_example_5(self):
        s = "({{{{}}}))"
        self.assertEqual(False, self.solution.isValid(s))

    def test_example_6(self):
        s = "{}{}{}"
        self.assertEqual(True, self.solution.isValid(s))

    def test_example_7(self):
        s = "){"
        self.assertEqual(False, self.solution.isValid(s))

    def test_example_8(self):
        s = ")(){}"
        self.assertEqual(False, self.solution.isValid(s))

    def test_example_9(self):
        s = "]()[]{}"
        self.assertEqual(False, self.solution.isValid(s))
