"""
Solution for LC#112: Path Sum
https://leetcode.com/problems/path-sum/
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
    def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right and root.val != targetSum:
            return False

        def _traversal(node: TreeNode, current_sum: int):
            if node:
                current_sum += node.val
                if current_sum == targetSum and not node.left and not node.right:
                    return True
                found = _traversal(node.left, current_sum)
                if found:
                    return True
                found = _traversal(node.right, current_sum)
                if found:
                    return True
            return False

        return _traversal(root, 0)


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_example_1(self):
        root = TreeNode(5)
        root.left = TreeNode(4)
        root.left.left = TreeNode(11)
        root.left.left.left = TreeNode(7)
        root.left.left.right = TreeNode(2)
        root.right = TreeNode(8)
        root.right.left = TreeNode(13)
        root.right.right = TreeNode(4)
        root.right.right.right = TreeNode(1)
        target_sum = 22
        self.assertEqual(True, self.solution.hasPathSum(root, target_sum))

    def test_example_2(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        target_sum = 5
        self.assertEqual(False, self.solution.hasPathSum(root, target_sum))

    def test_example_3(self):
        root = None
        target_sum = 0
        self.assertEqual(False, self.solution.hasPathSum(root, target_sum))

    def test_example_4(self):
        root = TreeNode(5)
        target_sum = 5
        self.assertEqual(True, self.solution.hasPathSum(root, target_sum))

    def test_example_5(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        target_sum = 1
        self.assertEqual(False, self.solution.hasPathSum(root, target_sum))
