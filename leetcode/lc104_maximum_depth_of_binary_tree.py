"""
Solution for LC#104: Maximum Depth of Binary Tree
https://leetcode.com/problems/maximum-depth-of-binary-tree/
"""
import unittest

from collections import Counter


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:

        counter = Counter()

        def _traversal(node: TreeNode):
            if node:
                counter["level"] += 1
                _traversal(node.left)
                _traversal(node.right)
                counter["maximum_depth"] = max(counter["level"], counter["maximum_depth"])
                counter["level"] -= 1

        _traversal(root)

        return counter["maximum_depth"]


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_example_1(self):
        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.right = TreeNode(7)
        root.right.left = TreeNode(15)
        self.assertEqual(3, self.solution.maxDepth(root))

    def test_example_2(self):
        root = TreeNode(1)
        root.right = TreeNode(2)
        self.assertEqual(2, self.solution.maxDepth(root))
