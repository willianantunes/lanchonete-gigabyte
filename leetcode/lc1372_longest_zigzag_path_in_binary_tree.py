"""
Solution for LC#1372: Longest ZigZag Path in a Binary Tree
https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/
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


class Solution:
    def longestZigZag(self, root: TreeNode | None) -> int:
        if not root.left and not root.right:
            return 0

        store = {"visited_nodes": 0}

        def _traverse(node: TreeNode, counter: int, is_left: bool):
            store["visited_nodes"] = max(store["visited_nodes"], counter)
            if node:
                _traverse(node.left, counter + 1 if not is_left else 1, True)
                _traverse(node.right, counter + 1 if is_left else 1, False)

        _traverse(root.left, 1, True)
        _traverse(root.right, 1, False)

        visited_nodes = store["visited_nodes"]
        # Zigzag length is defined as the number of nodes visited - 1.
        return visited_nodes - 1


class TestSolution(unittest.TestCase):
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

    def setUp(self) -> None:
        self.solution = Solution()

    def test_example_1(self):
        root = self.generate_tree([2, None, 1, 1, 1, None, None, 1, 1, None, 1, None, None, None, 1, None, 1])
        self.assertEqual(3, self.solution.longestZigZag(root))

    def test_example_2(self):
        root = self.generate_tree([1, 1, 1, None, 1, None, None, 1, 1, None, 1])
        self.assertEqual(4, self.solution.longestZigZag(root))

    def test_example_3(self):
        root = self.generate_tree([1])
        self.assertEqual(0, self.solution.longestZigZag(root))

    def test_example_4(self):
        root = self.generate_tree([1, None, 1, 1, 1, None, None, None, 1])
        self.assertEqual(2, self.solution.longestZigZag(root))

    def test_example_5(self):
        root = self.generate_tree([1, 1, 1, 1, None, None, 1])
        self.assertEqual(1, self.solution.longestZigZag(root))
