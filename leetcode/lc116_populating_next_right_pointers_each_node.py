"""
Solution for LC#1372: Longest ZigZag Path in a Binary Tree
https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/
"""
import unittest


class Node:
    def __init__(self, val: int = 0, left: "Node" = None, right: "Node" = None, next: "Node" = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

    def __str__(self):
        return str(self.val)

    def __repr__(self):
        return str(self.val)

    def __eq__(self, other: "Node"):
        if not other:
            return False

        def _traversal(node: "Node", store: list):
            if node:
                store.append(node.val)
                if node.next:
                    store.append(node.next.val)
                _traversal(node.left, store)
                _traversal(node.right, store)

        current_values = []
        other_values = []

        _traversal(self, store=current_values)
        _traversal(other, store=other_values)

        return current_values == other_values


class Solution:
    def connect(self, root: Node | None) -> Node | None:
        if not root:
            return
        queue = []
        current_level = 0
        levels = {}
        queue.append((root, current_level))
        while queue:
            node, level = queue.pop(0)
            nodes = levels.get(level, [])
            if level > current_level:
                current_level = level
            nodes.append(node)
            levels[level] = nodes
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))

        for key in levels.keys():
            if key != 0:
                nodes = levels[key]
                while nodes:
                    left, right = nodes.pop(0), nodes.pop(0)
                    left.next = right
                    if nodes:
                        nodes.insert(0, right)

        return root


class TestSolution(unittest.TestCase):
    def generate_tree(self, config: list[int | None]) -> Node:
        nodes = [Node(value) if value is not None else None for value in config]
        children = nodes[::-1]
        root = children.pop()
        for node in nodes:
            if node:
                if children:
                    node.left = children.pop()
                if children:
                    node.right = children.pop()
        return root

    def setUp(self) -> None:
        self.solution = Solution()

    def test_example_1(self):
        root = self.generate_tree([1, 2, 3, 4, 5, 6, 7])
        expected = self.generate_tree([1, 2, 3, 4, 5, 6, 7])
        expected.left.next = expected.right
        expected.left.left.next = expected.left.right
        expected.left.right.next = expected.right.left
        expected.right.left.next = expected.right.right
        a = expected == self.solution.connect(root)
        self.assertEqual(expected, self.solution.connect(root))
