"""
Solution for LC#206: Reverse Linked List
https://leetcode.com/problems/reverse-linked-list/
"""
import unittest


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __eq__(self, other: "ListNode") -> bool:
        current = self
        while current and other and current.val == other.val:
            current = current.next
            other = other.next
        if not current and not other:
            return True
        return False

    def __str__(self):
        return f"Current value: {self.val}"


class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        if not head or not head.next:
            return head

        stack = []
        while head:
            stack.append(head)
            head = head.next

        inverted_list = None
        last_node = stack.pop()
        while last_node:
            if not inverted_list:
                head = inverted_list = last_node
            else:
                last_node.next = None
                inverted_list.next = last_node
                inverted_list = last_node
            last_node = stack.pop() if stack else None

        return head


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def prepare_linked_list(self, items: list, position: int = None) -> ListNode | None:
        if not items:
            return None
        head_length = len(items)
        stored_head = None
        root = None
        last_node = None
        for index, value in enumerate(items):
            if index == 0:
                root = ListNode(value)
                last_node = root
            else:
                last_node.next = ListNode(value)
                last_node = last_node.next
            if position and position == index:
                stored_head = last_node
            if index == head_length - 1:
                last_node.next = stored_head
        return root

    def test_example_1(self):
        head = self.prepare_linked_list([1, 2, 3, 4, 5])
        expected = self.prepare_linked_list([5, 4, 3, 2, 1])
        self.assertEqual(expected, self.solution.reverseList(head))

    def test_example_2(self):
        head = self.prepare_linked_list([1, 2])
        expected = self.prepare_linked_list([2, 1])
        self.assertEqual(expected, self.solution.reverseList(head))

    def test_example_3(self):
        head = self.prepare_linked_list([1])
        expected = self.prepare_linked_list([1])
        self.assertEqual(expected, self.solution.reverseList(head))

    def test_example_4(self):
        head = self.prepare_linked_list([1, 1, 1, 1, 1])
        expected = self.prepare_linked_list([1, 1, 1, 1, 1])
        self.assertEqual(expected, self.solution.reverseList(head))
