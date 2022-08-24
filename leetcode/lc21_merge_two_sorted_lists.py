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
        if list1 is None and list2 is None:
            return None
        if list1 is None and list2 is not None:
            return list2
        if list1 is not None and list2 is None:
            return list1

        head = None
        dummy_node = None
        pointer_i, pointer_j = list1.val, list2.val

        while pointer_i is not None or pointer_j is not None:
            if pointer_i is None and pointer_j is not None:
                previous_dummy_node = dummy_node
                dummy_node = ListNode(pointer_j, list2.next)
                previous_dummy_node.next = dummy_node
                break
            elif pointer_i is not None and pointer_j is None:
                previous_dummy_node = dummy_node
                dummy_node = ListNode(pointer_i, list1.next)
                previous_dummy_node.next = dummy_node
                break
            elif pointer_i > pointer_j:
                if head is None:
                    head = dummy_node = previous_dummy_node = ListNode(pointer_j)
                else:
                    previous_dummy_node = dummy_node
                    dummy_node = ListNode(pointer_j)
                previous_dummy_node.next = dummy_node

                next_list2 = list2.next
                pointer_j = next_list2.val if next_list2 else None
                list2 = next_list2
            else:
                if head is None:
                    head = dummy_node = previous_dummy_node = ListNode(pointer_i)
                else:
                    previous_dummy_node = dummy_node
                    dummy_node = ListNode(pointer_i)
                previous_dummy_node.next = dummy_node

                next_list1 = list1.next
                pointer_i = next_list1.val if next_list1 else None
                list1 = next_list1

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
