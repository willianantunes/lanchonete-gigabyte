"""
Solution for LC#141: Linked List Cycle
https://leetcode.com/problems/linked-list-cycle/
"""
import unittest

from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        database_of_addresses = {}

        while head:
            current_address = id(head)
            current_counter = database_of_addresses.get(current_address, 0) + 1
            database_of_addresses[current_address] = current_counter

            if current_counter > 1:
                return True
            head = head.next if head.next else None

        return False


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def prepare_linked_list(self, items: list, position: int) -> ListNode:
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
            if position == index:
                stored_head = last_node
            if index == head_length - 1:
                last_node.next = stored_head
        return root

    def test_example_1(self):
        head = [3, 2, 0, -4]
        pos = 1
        root = self.prepare_linked_list(head, pos)
        self.assertEqual(True, self.solution.hasCycle(root))

    def test_example_2(self):
        head = [1, 2]
        pos = 0
        root = self.prepare_linked_list(head, pos)
        self.assertEqual(True, self.solution.hasCycle(root))

    def test_example_3(self):
        head = [1]
        pos = -1
        root = self.prepare_linked_list(head, pos)
        self.assertEqual(False, self.solution.hasCycle(root))

    def test_example_4(self):
        head = [
            -21,
            10,
            17,
            8,
            4,
            26,
            5,
            35,
            33,
            -7,
            -16,
            27,
            -12,
            6,
            29,
            -12,
            5,
            9,
            20,
            14,
            14,
            2,
            13,
            -24,
            21,
            23,
            -21,
            5,
        ]
        pos = -1
        root = self.prepare_linked_list(head, pos)
        self.assertEqual(False, self.solution.hasCycle(root))
