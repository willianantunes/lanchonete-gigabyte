"""
Solution for LC#144: Binary Tree Preorder Traversal
https://leetcode.com/problems/binary-tree-preorder-traversal/
"""
import unittest


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: TreeNode | None) -> list[int]:
        if not root:
            return []

        found_values = []

        def _preorder_traversal(node):
            if node:
                found_values.append(node.val)
                _preorder_traversal(node.left)
                _preorder_traversal(node.right)

        _preorder_traversal(root)

        return found_values


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_example_1(self):
        node_3 = TreeNode(3)
        node_2 = TreeNode(2, left=node_3)
        root = TreeNode(1, right=node_2)
        self.assertEqual([1, 2, 3], self.solution.preorderTraversal(root))

    def test_example_2(self):
        root = TreeNode(1)
        self.assertEqual([1], self.solution.preorderTraversal(root))

    def test_example_3(self):
        node_5 = TreeNode(5)
        node_4 = TreeNode(4)
        node_3 = TreeNode(3)
        node_2 = TreeNode(2, left=node_4, right=node_5)
        root = TreeNode(1, left=node_2, right=node_3)
        self.assertEqual([1, 2, 4, 5, 3], self.solution.preorderTraversal(root))
