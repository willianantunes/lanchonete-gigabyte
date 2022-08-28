"""
Solution for LC#232: Implement Queue using Stacks
https://leetcode.com/problems/implement-queue-using-stacks/
"""
import unittest


class MyQueue:
    def __init__(self):
        self.stack_front = []
        self.stack_rear = []

    def push(self, x: int) -> None:
        self.stack_front.append(x)

    def pop(self) -> int:
        while self.stack_front:
            value = self.stack_front.pop()
            self.stack_rear.append(value)
        value_to_be_returned = self.stack_rear.pop()
        while self.stack_rear:
            value = self.stack_rear.pop()
            self.stack_front.append(value)
        return value_to_be_returned

    def peek(self) -> int:
        while self.stack_front:
            value = self.stack_front.pop()
            self.stack_rear.append(value)
        value_to_be_returned = self.stack_rear[-1]
        while self.stack_rear:
            value = self.stack_rear.pop()
            self.stack_front.append(value)
        return value_to_be_returned

    def empty(self) -> bool:
        return len(self.stack_front) == 0 and len(self.stack_rear) == 0

    def __str__(self):
        return str(self.stack_front)


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.queue = MyQueue()

    def test_example_1(self):
        self.queue.push(1)
        self.assertEqual("[1]", str(self.queue))
        self.queue.push(2)
        self.assertEqual("[1, 2]", str(self.queue))
        self.assertEqual(1, self.queue.peek())
        self.assertEqual(1, self.queue.pop())
        self.assertEqual("[2]", str(self.queue))
        self.assertFalse(self.queue.empty())

    def test_example_2(self):
        self.queue.push(2)
        self.assertEqual(2, self.queue.peek())
        self.queue.push(3)
        self.assertEqual(2, self.queue.peek())
        self.queue.push(4)
        self.assertEqual("[2, 3, 4]", str(self.queue))
        self.assertEqual(2, self.queue.pop())
        self.assertEqual(3, self.queue.peek())
        self.assertEqual("[3, 4]", str(self.queue))
        self.assertFalse(self.queue.empty())
        self.assertEqual(3, self.queue.pop())
        self.assertEqual(4, self.queue.pop())
        self.assertTrue(self.queue.empty())
