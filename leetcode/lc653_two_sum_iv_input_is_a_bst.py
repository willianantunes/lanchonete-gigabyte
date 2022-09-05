"""
Solution for LC#653: Two Sum IV - Input is a BST
https://leetcode.com/problems/two-sum-iv-input-is-a-bst/
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
    def findTarget(self, root: TreeNode | None, k: int) -> bool:

        values = []

        def _traversal(node: TreeNode):
            if node:
                values.append(node.val)
                _traversal(node.left)
                _traversal(node.right)

        _traversal(root)

        for index_base, base in enumerate(values):
            for index_value, value in enumerate(values):
                if index_base != index_value and base + value == k:
                    return True

        return False


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_example_1(self):
        root = TreeNode(5)
        root.left = TreeNode(3)
        root.left.left = TreeNode(2)
        root.left.right = TreeNode(4)
        root.right = TreeNode(6)
        root.right.right = TreeNode(7)
        k = 9
        self.assertEqual(True, self.solution.findTarget(root, k))

    def test_example_2(self):
        root = TreeNode(5)
        root.left = TreeNode(3)
        root.left.left = TreeNode(2)
        root.left.right = TreeNode(4)
        root.right = TreeNode(6)
        root.right.right = TreeNode(7)
        k = 28
        self.assertEqual(False, self.solution.findTarget(root, k))

    def test_example_3(self):
        root = TreeNode(1)
        k = 2
        self.assertEqual(False, self.solution.findTarget(root, k))
