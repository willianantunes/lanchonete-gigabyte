"""
Solution for LC#617: Merge Two Binary Trees
https://leetcode.com/problems/merge-two-binary-trees/
"""
import unittest


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)

    def __repr__(self):
        return str(self.val)

    def __eq__(self, other: "TreeNode"):
        if not other:
            return False

        def _traversal(node: "TreeNode", store: list):
            if node:
                store.append(node.val)
                if node.right:
                    store.append(node.right.val)
                _traversal(node.left, store)
                _traversal(node.right, store)

        current_values = []
        other_values = []

        _traversal(self, store=current_values)
        _traversal(other, store=other_values)

        return current_values == other_values


class Solution:
    def mergeTrees(self, root1: TreeNode | None, root2: TreeNode | None) -> TreeNode | None:
        if not root1 and not root2:
            return
        if root1 and not root2:
            return root1
        if not root1 and root2:
            return root2
        head = TreeNode()
        queue = [(root1, head), (root2, head)]
        while queue:
            node, current_node = queue.pop(0)
            if node is not None:
                current_node.val += node.val
                if node.left:
                    if not current_node.left:
                        current_node.left = TreeNode()
                    queue.append((node.left, current_node.left))
                if node.right:
                    if not current_node.right:
                        current_node.right = TreeNode()
                    queue.append((node.right, current_node.right))
        return head


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def generate_tree(self, config: list[int | None]) -> TreeNode:
        nodes = [TreeNode(value) if value is not None else None for value in config]
        children = nodes[::-1]
        root = children.pop()
        for node in nodes:
            if node:
                if children:
                    node.left = children.pop()
                if children:
                    node.right = children.pop()
        return root

    def test_example_1(self):
        root1 = self.generate_tree([1, 3, 2, 5])
        root2 = self.generate_tree([2, 1, 3, None, 4, None, 7])
        expected = self.generate_tree([3, 4, 5, 5, 4, None, 7])
        self.assertEqual(expected, self.solution.mergeTrees(root1, root2))

    def test_example_2(self):
        root1 = self.generate_tree([1])
        root2 = self.generate_tree([1, 2])
        expected = self.generate_tree([2, 2])
        self.assertEqual(expected, self.solution.mergeTrees(root1, root2))
