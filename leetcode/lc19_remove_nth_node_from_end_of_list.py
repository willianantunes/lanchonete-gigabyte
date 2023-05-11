"""
Solution for LC#19: Remove Nth Node From End of List
https://leetcode.com/problems/remove-nth-node-from-end-of-list/
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
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        if not head.next and n == 1:
            return
        current_length = 0
        current_node = head
        while current_node:
            current_length += 1
            current_node = current_node.next

        target_node = current_length - n
        counter = 0
        current_node = previous_node = head
        while current_node:
            if counter == target_node and counter == 0:
                head = head.next
                break
            elif counter == target_node:
                previous_node.next = current_node.next
                break
            else:
                previous_node = current_node
                current_node = current_node.next
                counter += 1

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
        n = 2
        self.assertEqual(self.prepare_linked_list([1, 2, 3, 5]), self.solution.removeNthFromEnd(head, n))

    def test_example_2(self):
        head = self.prepare_linked_list([1])
        n = 1
        self.assertEqual(self.prepare_linked_list([]), self.solution.removeNthFromEnd(head, n))

    def test_example_3(self):
        head = self.prepare_linked_list([1, 2])
        n = 1
        self.assertEqual(self.prepare_linked_list([1]), self.solution.removeNthFromEnd(head, n))

    def test_example_4(self):
        head = self.prepare_linked_list([1, 2, 3, 4, 5])
        n = 1
        self.assertEqual(self.prepare_linked_list([1, 2, 3, 4]), self.solution.removeNthFromEnd(head, n))

    def test_example_5(self):
        head = self.prepare_linked_list([1, 2, 3, 4, 5])
        n = 3
        self.assertEqual(self.prepare_linked_list([1, 2, 4, 5]), self.solution.removeNthFromEnd(head, n))

    def test_example_6(self):
        head = self.prepare_linked_list([1, 2, 3, 4, 5])
        n = 4
        self.assertEqual(self.prepare_linked_list([1, 3, 4, 5]), self.solution.removeNthFromEnd(head, n))

    def test_example_7(self):
        head = self.prepare_linked_list([1, 2, 3, 4, 5])
        n = 5
        self.assertEqual(self.prepare_linked_list([2, 3, 4, 5]), self.solution.removeNthFromEnd(head, n))
