"""
Solution for LC#700. Search in a Binary Search Tree
https://leetcode.com/problems/search-in-a-binary-search-tree/
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
    def searchBST(self, root: TreeNode | None, val: int) -> TreeNode | None:
        if not root:
            return None
        if not root.left and not root.right and root.val != val:
            return None

        def _traversal(node: TreeNode):
            if node:
                if node.val == val:
                    return node
                found_node = _traversal(node.left)
                if found_node:
                    return found_node
                found_node = _traversal(node.right)
                if found_node:
                    return found_node

        return _traversal(root)


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_example_1(self):
        root = TreeNode(4)
        root.left = TreeNode(2)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(3)
        root.right = TreeNode(7)
        val = 2
        expected = TreeNode(2)
        expected.left = TreeNode(1)
        expected.right = TreeNode(3)
        self.assertEqual(expected, self.solution.searchBST(root, val))

    def test_example_2(self):
        root = TreeNode(4)
        root.left = TreeNode(2)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(3)
        root.right = TreeNode(7)
        val = 5
        self.assertEqual(None, self.solution.searchBST(root, val))
