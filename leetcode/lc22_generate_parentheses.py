"""
Solution for LC#22: Generate Parentheses
https://leetcode.com/problems/generate-parentheses/
String / Dynamic Programming / Backtracking / Stack
"""
import unittest


class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        parentheses = []
        stack = []

        initial_number_of_opening = 1
        initial_number_of_closing = 0
        entry = (initial_number_of_opening, initial_number_of_closing, "(")
        stack.append(entry)

        while stack:
            number_of_opening, number_of_closing, value = stack.pop()

            invalid_configuration = number_of_opening > n or number_of_closing > n
            if invalid_configuration:
                continue

            valid_final_configuration = number_of_opening == n and number_of_closing == n
            if valid_final_configuration:
                parentheses.append(value)

            if number_of_opening < n:
                stack.append((number_of_opening + 1, number_of_closing, value + "("))
            if number_of_closing < number_of_opening:
                stack.append((number_of_opening, number_of_closing + 1, value + ")"))

        return parentheses


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_example_1(self):
        n = 3
        expected_result = ["((()))", "(()())", "(())()", "()(())", "()()()"]
        self.assertEqual(set(expected_result), set(self.solution.generateParenthesis(n)))

    def test_example_2(self):
        n = 1
        self.assertEqual(["()"], self.solution.generateParenthesis(n))
