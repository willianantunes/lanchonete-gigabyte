"""
Solution for LC#150: Evaluate Reverse Polish Notation
https://leetcode.com/problems/evaluate-reverse-polish-notation/
"""
import unittest


class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        number_of_tokens = len(tokens)
        if number_of_tokens == 1:
            return int(tokens[0])

        operations = {
            "*": lambda left, right: left * right,
            "+": lambda left, right: left + right,
            "-": lambda left, right: left - right,
            "/": lambda left, right: int(left / right),
        }

        stack = []
        for token in tokens:
            is_operator = token in operations
            if is_operator:
                right, left = stack.pop(), stack.pop()
                result = operations[token](int(left), int(right))
                stack.append(result)
            else:
                stack.append(token)

        return stack.pop()


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_example_1(self):
        tokens = ["2", "1", "+", "3", "*"]
        self.assertEqual(9, self.solution.evalRPN(tokens))

    def test_example_2(self):
        tokens = ["4", "13", "5", "/", "+"]
        self.assertEqual(6, self.solution.evalRPN(tokens))

    def test_example_3(self):
        tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
        self.assertEqual(22, self.solution.evalRPN(tokens))
