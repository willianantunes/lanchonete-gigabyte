"""
Solution for LC#876: Middle of the Linked List
https://leetcode.com/problems/middle-of-the-linked-list/
"""
import unittest


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f"{self.val} -> {self.next}"

    def __repr__(self):
        return f"{self.val} -> {self.next}"

    def __eq__(self, other: "ListNode") -> bool:
        current = self
        while current and other and current.val == other.val:
            current = current.next
            other = other.next
        if not current and not other:
            return True
        return False


class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        node_count = 0
        current_node = head
        while current_node:
            node_count += 1
            current_node = current_node.next
        is_even = node_count % 2 == 0
        node_count += 2 if is_even else 1
        middle_node_index = node_count // 2
        node_count = 0
        while head:
            node_count += 1
            if node_count == middle_node_index:
                return head
            head = head.next


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
        self.assertEqual(self.prepare_linked_list([3, 4, 5]), self.solution.middleNode(head))

    def test_example_2(self):
        head = self.prepare_linked_list([1, 2, 3, 4, 5, 6])
        self.assertEqual(self.prepare_linked_list([4, 5, 6]), self.solution.middleNode(head))

    def test_example_3(self):
        head = self.prepare_linked_list([1, 2, 3])
        self.assertEqual(self.prepare_linked_list([2, 3]), self.solution.middleNode(head))

    def test_example_4(self):
        head = self.prepare_linked_list([1])
        self.assertEqual(self.prepare_linked_list([1]), self.solution.middleNode(head))

    def test_example_5(self):
        head = self.prepare_linked_list([1, 2])
        self.assertEqual(self.prepare_linked_list([2]), self.solution.middleNode(head))
