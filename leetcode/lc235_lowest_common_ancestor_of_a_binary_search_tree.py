"""
Solution for LC#235: Lowest Common Ancestor of a Binary Search Tree
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
"""
import unittest

from collections import Counter


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
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        class Holder:
            pass

        holder = Holder()
        holder.values_from_above_p: list[TreeNode] | None = None
        holder.values_from_above_q: list[TreeNode] | None = None

        def _traversal(node: TreeNode, values_from_above):
            if node:
                if node.val == p.val:
                    holder.values_from_above_p = values_from_above
                elif node.val == q.val:
                    holder.values_from_above_q = values_from_above
                else:
                    _traversal(node.left, values_from_above + [node])
                    _traversal(node.right, values_from_above + [node])

        _traversal(root, [])

        if not holder.values_from_above_p and not holder.values_from_above_q:
            if root.val == p.val:
                return p
            else:
                return q
        elif holder.values_from_above_p and not holder.values_from_above_q:
            return p
        elif not holder.values_from_above_p and holder.values_from_above_q:
            return q
        else:
            max_index = len(holder.values_from_above_p) - 1
            values_from_above_q_length = len(holder.values_from_above_q)
            for index, _ in enumerate(holder.values_from_above_p):
                if index < values_from_above_q_length:
                    if holder.values_from_above_p[index] != holder.values_from_above_q[index]:
                        return holder.values_from_above_p[index - 1]
                else:
                    return holder.values_from_above_p[index - 1]
            return holder.values_from_above_p[max_index]


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_example_1(self):
        root = TreeNode(6)
        root.left = TreeNode(2)
        root.left.left = TreeNode(0)
        root.left.right = TreeNode(4)
        root.left.right.left = TreeNode(3)
        root.left.right.right = TreeNode(5)
        root.right = TreeNode(8)
        root.right.left = TreeNode(7)
        root.right.right = TreeNode(9)
        p = root.left
        q = root.right
        self.assertEqual(root, self.solution.lowestCommonAncestor(root, p, q))

    def test_example_2(self):
        root = TreeNode(6)
        root.left = TreeNode(2)
        root.left.left = TreeNode(0)
        root.left.right = TreeNode(4)
        root.left.right.left = TreeNode(3)
        root.left.right.right = TreeNode(5)
        root.right = TreeNode(8)
        root.right.left = TreeNode(7)
        root.right.right = TreeNode(9)
        p = root.left
        q = root.left.right
        self.assertEqual(root.left, self.solution.lowestCommonAncestor(root, p, q))

    def test_example_3(self):
        root = TreeNode(2)
        root.left = TreeNode(1)
        p = root
        q = root.left
        self.assertEqual(root, self.solution.lowestCommonAncestor(root, p, q))

    def test_example_4(self):
        root = TreeNode(6)
        root.left = TreeNode(2)
        root.left.left = TreeNode(0)
        root.left.right = TreeNode(4)
        root.left.right.left = TreeNode(3)
        root.left.right.right = TreeNode(5)
        root.right = TreeNode(8)
        root.right.left = TreeNode(7)
        root.right.right = TreeNode(9)
        p = root.left.right.left
        q = root.left.right.right
        self.assertEqual(root.left.right, self.solution.lowestCommonAncestor(root, p, q))

    def test_example_5(self):
        root = TreeNode(3)
        root.left = TreeNode(1)
        root.left.right = TreeNode(2)
        root.right = TreeNode(4)
        p = root.left.right
        q = root.right
        self.assertEqual(root, self.solution.lowestCommonAncestor(root, p, q))

    def test_example_6(self):
        root = TreeNode(41)
        root.left = TreeNode(37)
        root.left.right = TreeNode(39)
        root.left.right.left = TreeNode(38)
        root.left.right.right = TreeNode(40)
        root.left.left = TreeNode(24)
        root.right = TreeNode(44)
        root.right.left = TreeNode(42)
        root.right.left.right = TreeNode(43)
        root.right.right = TreeNode(48)
        root.right.right.left = TreeNode(46)
        root.right.right.right = TreeNode(49)
        p = root.left.right.right
        q = root.right.right.left
        self.assertEqual(root, self.solution.lowestCommonAncestor(root, p, q))
