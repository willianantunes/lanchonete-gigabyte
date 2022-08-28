"""
Solution for LC#94: Binary Tree Inorder Traversal
https://leetcode.com/problems/binary-tree-inorder-traversal/
"""
import unittest


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        if not root:
            return []

        found_values = []

        def _inorder_traversal(node):
            if node:
                _inorder_traversal(node.left)
                found_values.append(node.val)
                _inorder_traversal(node.right)

        _inorder_traversal(root)

        return found_values


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_example_1(self):
        node_3 = TreeNode(3)
        node_2 = TreeNode(2, left=node_3)
        root = TreeNode(1, right=node_2)
        self.assertEqual([1, 3, 2], self.solution.inorderTraversal(root))

    def test_example_2(self):
        root = TreeNode(1)
        self.assertEqual([1], self.solution.inorderTraversal(root))

    def test_example_3(self):
        node_5 = TreeNode(5)
        node_4 = TreeNode(4)
        node_3 = TreeNode(3)
        node_2 = TreeNode(2, left=node_4, right=node_5)
        root = TreeNode(1, left=node_2, right=node_3)
        self.assertEqual([4, 2, 5, 1, 3], self.solution.inorderTraversal(root))
