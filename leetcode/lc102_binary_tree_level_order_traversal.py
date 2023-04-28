"""
Solution for LC#102: Binary Tree Level Order Traversal
https://leetcode.com/problems/binary-tree-level-order-traversal/
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
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if not root:
            return []

        queue = [root]
        nodes_grouped_by_level = []

        while queue:
            found_nodes = []
            number_of_nodes_to_be_seen = len(queue)
            for _ in range(number_of_nodes_to_be_seen):
                node = queue.pop(0)
                found_nodes.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            nodes_grouped_by_level.append(found_nodes)

        return nodes_grouped_by_level


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
        node_3 = TreeNode(3)
        node_2 = TreeNode(2, left=node_3)
        root = TreeNode(1, right=node_2)
        self.assertEqual([[1], [2], [3]], self.solution.levelOrder(root))

    def test_example_2(self):
        node_5 = TreeNode(5)
        node_4 = TreeNode(4)
        node_3 = TreeNode(3)
        node_2 = TreeNode(2, left=node_4, right=node_5)
        root = TreeNode(1, left=node_2, right=node_3)
        self.assertEqual([[1], [2, 3], [4, 5]], self.solution.levelOrder(root))

    def test_example_3(self):
        node_7 = TreeNode(7)
        node_15 = TreeNode(15)
        node_20 = TreeNode(20, left=node_15, right=node_7)
        node_9 = TreeNode(9)
        root = TreeNode(3, left=node_9, right=node_20)
        self.assertEqual([[3], [9, 20], [15, 7]], self.solution.levelOrder(root))

    def test_example_4(self):
        root = TreeNode(33)
        self.assertEqual([[33]], self.solution.levelOrder(root))

    def test_example_5(self):
        root = self.generate_tree([2, None, 1, 1, 1, 3, 4, 1, 1, 10, 1, 8, 33, 31, 1, 24, 1])
        self.assertEqual([[2], [1], [1, 1], [3, 4, 1, 1], [10, 1, 8, 33, 31, 1, 24, 1]], self.solution.levelOrder(root))
