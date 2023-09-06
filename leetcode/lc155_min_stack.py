"""
Solution for LC#155: Min Stack
https://leetcode.com/problems/min-stack/
"""
import unittest


class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append((val, val))
        else:
            _, previous_minimum_value = self.stack[-1]
            minimum_value = val if val < previous_minimum_value else previous_minimum_value
            self.stack.append((val, minimum_value))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = MinStack()

    def test_example_1(self):
        self.solution.push(-2)
        self.solution.push(0)
        self.solution.push(-3)
        self.assertEqual(-3, self.solution.getMin())
        self.solution.pop()
        self.assertEqual(0, self.solution.top())
        self.assertEqual(-2, self.solution.getMin())
