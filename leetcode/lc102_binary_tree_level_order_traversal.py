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


class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if not root:
            return []

        class LevelHolder:
            pass

        evaluation = {}
        level_holder = LevelHolder()
        level_holder.current = -1

        def _navigate_tree(node):
            if node:
                level_holder.current += 1
                found_values = evaluation.get(level_holder.current, [])
                found_values.append(node.val)
                evaluation[level_holder.current] = found_values
                _navigate_tree(node.left)
                _navigate_tree(node.right)
                level_holder.current -= 1

        _navigate_tree(root)

        level = []
        for index in evaluation.keys():
            level.append([])
            level[index] = evaluation[index]

        return level


class TestSolution(unittest.TestCase):
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
