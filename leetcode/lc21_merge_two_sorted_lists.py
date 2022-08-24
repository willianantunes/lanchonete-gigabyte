"""
Solution for LC#21: Merge Two Sorted Lists
https://leetcode.com/problems/merge-two-sorted-lists/
"""
import unittest

from typing import Optional


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
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None
        if not list1 and list2:
            return list2
        if list1 and not list2:
            return list1

        head = current = None

        while list1 and list2:
            if list1.val > list2.val:
                if not head:
                    head = current = list2
                else:
                    current.next = list2
                    current = current.next
                list2 = list2.next
            else:
                if not head:
                    head = current = list1
                else:
                    current.next = list1
                    current = current.next
                list1 = list1.next

        if list1 or list2:
            current.next = list1 if list1 else list2

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
        list1 = self.prepare_linked_list([1, 2, 4])
        list2 = self.prepare_linked_list([1, 3, 4])
        expected = self.prepare_linked_list([1, 1, 2, 3, 4, 4])
        self.assertEqual(expected, self.solution.mergeTwoLists(list1, list2))

    def test_example_2(self):
        list1 = self.prepare_linked_list([])
        list2 = self.prepare_linked_list([])
        self.assertEqual(None, self.solution.mergeTwoLists(list1, list2))

    def test_example_3(self):
        list1 = None
        list2 = self.prepare_linked_list([0])
        expected = self.prepare_linked_list([0])
        self.assertEqual(expected, self.solution.mergeTwoLists(list1, list2))

    def test_example_4(self):
        list1 = self.prepare_linked_list([1, 2, 4])
        list2 = self.prepare_linked_list([0, 3, 3])
        expected = self.prepare_linked_list([0, 1, 2, 3, 3, 4])
        self.assertEqual(expected, self.solution.mergeTwoLists(list1, list2))

    def test_example_5(self):
        list1 = self.prepare_linked_list([5])
        list2 = self.prepare_linked_list([1, 2, 4])
        expected = self.prepare_linked_list([1, 2, 4, 5])
        self.assertEqual(expected, self.solution.mergeTwoLists(list1, list2))

    def test_example_6(self):
        list1 = self.prepare_linked_list([-8, -6, -6, -3, 0, 4, 4, 8])
        list2 = self.prepare_linked_list([-7, -4, -3, 0, 5])
        expected = self.prepare_linked_list([-8, -7, -6, -6, -4, -3, -3, 0, 0, 4, 4, 5, 8])
        self.assertEqual(expected, self.solution.mergeTwoLists(list1, list2))
