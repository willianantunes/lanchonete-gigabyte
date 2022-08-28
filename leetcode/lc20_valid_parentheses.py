"""
Solution for LC#20: Valid Parentheses
https://leetcode.com/problems/valid-parentheses/
"""
import unittest


class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False

        def _is_valid(stack, current_value):
            is_inner_valid = True
            while stack and is_inner_valid:
                next_value = stack[-1]
                if ")" == next_value or "}" == next_value or "]" == next_value:
                    is_inner_valid = _is_valid(stack, stack.pop())
                else:
                    break
                if not is_inner_valid:
                    return is_inner_valid
            if not stack:
                return False
            right_value_as_unicode_point = ord(current_value)
            left_value_as_unicode_point = ord(stack.pop())
            is_one_type_valid = right_value_as_unicode_point - left_value_as_unicode_point == 1
            are_two_types_valid = right_value_as_unicode_point - left_value_as_unicode_point == 2
            if are_two_types_valid or is_one_type_valid:
                return True
            return False

        stack_of_values = list(s)
        last_evaluation = True
        while stack_of_values and last_evaluation:
            last_evaluation = _is_valid(stack_of_values, stack_of_values.pop())
        return last_evaluation


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
