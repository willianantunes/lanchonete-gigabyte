"""
Solution for LC#226: Invert Binary Tree
https://leetcode.com/problems/invert-binary-tree/
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
        current_values = []
        self._traversal(self, store=current_values)
        return str(current_values)

    def __eq__(self, other: "TreeNode"):
        if not other:
            return False

        def _traversal(node: "TreeNode", store: list):
            if node:
                store.append(node.val)
                _traversal(node.left, store)
                _traversal(node.right, store)

        current_values = []
        other_values = []

        self._traversal(self, store=current_values)
        self._traversal(other, store=other_values)

        return current_values == other_values

    def _traversal(self, node: "TreeNode", **kwargs):
        if node:
            store = kwargs.get("store")
            if store is not None:
                store.append(node.val)
            self._traversal(node.left, **kwargs)
            self._traversal(node.right, **kwargs)


class Solution:
    def invertTree(self, root: TreeNode | None) -> TreeNode | None:
        if not root:
            return None
        if root and not root.left and not root.right:
            return root

        def _traversal(node: TreeNode, new_node: TreeNode):
            if node:
                new_node.right = TreeNode(node.left.val) if node.left else None
                _traversal(node.left, new_node.right)
                new_node.left = TreeNode(node.right.val) if node.right else None
                _traversal(node.right, new_node.left)

        new_right = TreeNode(root.left.val) if root.left else None
        _traversal(root.left, new_right)
        new_left = TreeNode(root.right.val) if root.right else None
        _traversal(root.right, new_left)
        root.right = new_right
        root.left = new_left

        return root


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_example_1(self):
        root = TreeNode(4)
        root.left = TreeNode(2)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(3)
        root.right = TreeNode(7)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(9)

        expected = TreeNode(4)
        expected.right = TreeNode(2)
        expected.right.right = TreeNode(1)
        expected.right.left = TreeNode(3)
        expected.left = TreeNode(7)
        expected.left.left = TreeNode(9)
        expected.left.right = TreeNode(6)
        self.assertEqual(expected, self.solution.invertTree(root))

    def test_example_2(self):
        root = TreeNode(2)
        root.left = TreeNode(1)
        root.right = TreeNode(3)

        expected = TreeNode(2)
        expected.right = TreeNode(1)
        expected.left = TreeNode(3)
        self.assertEqual(expected, self.solution.invertTree(root))

    def test_example_3(self):
        root = None
        self.assertEqual(None, self.solution.invertTree(root))

    def test_example_4(self):
        root = TreeNode(1)
        root.left = TreeNode(2)

        expected = TreeNode(1)
        expected.right = TreeNode(2)
        self.assertEqual(expected, self.solution.invertTree(root))

    def test_example_5(self):
        root = TreeNode(4)
        root.left = TreeNode(1)
        root.left.left = TreeNode(2)
        root.left.left.left = TreeNode(3)

        expected = TreeNode(4)
        expected.right = TreeNode(1)
        expected.right.right = TreeNode(2)
        expected.right.right.right = TreeNode(3)
        self.assertEqual(expected, self.solution.invertTree(root))
