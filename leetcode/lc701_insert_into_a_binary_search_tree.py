"""
Solution for LC#701: Insert into a Binary Search Tree
https://leetcode.com/problems/insert-into-a-binary-search-tree/
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
    def insertIntoBST(self, root: TreeNode | None, val: int) -> TreeNode | None:
        if not root:
            return TreeNode(val)
        if root and not root.left and not root.right:
            if val < root.val:
                root.left = TreeNode(val)
            else:
                root.right = TreeNode(val)
            return root

        def _traversal(node: TreeNode):
            if node:
                if val < node.val and not node.left:
                    node.left = TreeNode(val)
                    return True
                elif val > node.val and not node.right:
                    node.right = TreeNode(val)
                    return True
                elif val < node.val:
                    inserted = _traversal(node.left)
                    if inserted:
                        return True
                else:
                    inserted = _traversal(node.right)
                    if inserted:
                        return True
            return False

        _traversal(root)

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
        val = 5
        expected = TreeNode(4)
        expected.left = TreeNode(2)
        expected.left.left = TreeNode(1)
        expected.left.right = TreeNode(3)
        expected.right = TreeNode(7)
        expected.right.left = TreeNode(val)
        self.assertEqual(expected, self.solution.insertIntoBST(root, val))
