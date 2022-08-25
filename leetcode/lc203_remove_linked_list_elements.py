"""
Solution for LC#203: Remove Linked List Elements
https://leetcode.com/problems/remove-linked-list-elements/
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
    def removeElements(self, head: ListNode | None, val: int) -> ListNode | None:
        pointer_head = None
        latest_valid_node = None

        while head:
            if head.val == val:
                if latest_valid_node:
                    latest_valid_node.next = None
                head = head.next
            else:
                if not pointer_head:
                    pointer_head = latest_valid_node = head
                else:
                    if latest_valid_node:
                        latest_valid_node.next = head
                    latest_valid_node = head
                head = head.next

        return pointer_head if pointer_head and pointer_head.val != val else None


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
        head = self.prepare_linked_list([1, 2, 6, 3, 4, 5, 6])
        val = 6
        expected = self.prepare_linked_list([1, 2, 3, 4, 5])
        self.assertEqual(expected, self.solution.removeElements(head, val))

    def test_example_2(self):
        head = self.prepare_linked_list([])
        val = 1
        expected = None
        self.assertEqual(expected, self.solution.removeElements(head, val))

    def test_example_3(self):
        head = self.prepare_linked_list([7, 7, 7, 7])
        val = 7
        expected = None
        self.assertEqual(expected, self.solution.removeElements(head, val))

    def test_example_4(self):
        head = self.prepare_linked_list([1])
        val = 1
        expected = None
        self.assertEqual(expected, self.solution.removeElements(head, val))

    def test_example_5(self):
        head = self.prepare_linked_list([1, 2])
        val = 1
        expected = self.prepare_linked_list([2])
        self.assertEqual(expected, self.solution.removeElements(head, val))
