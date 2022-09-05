"""
Solution for LC#98: Validate Binary Search Tree
https://leetcode.com/problems/validate-binary-search-tree/
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
    def isValidBST(self, root: TreeNode | None) -> bool:
        if not root:
            return False
        if not root.left and not root.right:
            return True
        if root.left and root.left.val >= root.val:
            return False
        if root.right and root.right.val <= root.val:
            return False

        def _is_valid_bst(node: TreeNode, values_from_above):
            if node:
                invalid_current_value = False
                for value, direction in values_from_above:
                    if direction == "left" and node.val >= value:
                        invalid_current_value = True
                        break
                    elif direction == "right" and node.val <= value:
                        invalid_current_value = True
                        break
                if invalid_current_value:
                    return False
                if node.left:
                    if node.left.val >= node.val:
                        return False
                elif node.right:
                    if node.right.val <= node.val:
                        return False
                is_valid = _is_valid_bst(node.left, values_from_above + [(node.val, "left")])
                if not is_valid:
                    return False
                is_valid = _is_valid_bst(node.right, values_from_above + [(node.val, "right")])
                if not is_valid:
                    return False
            return True

        return _is_valid_bst(root, [])


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_example_1(self):
        root = TreeNode(2)
        root.left = TreeNode(1)
        root.right = TreeNode(3)
        self.assertEqual(True, self.solution.isValidBST(root))

    def test_example_2(self):
        root = TreeNode(5)
        root.left = TreeNode(1)
        root.right = TreeNode(4)
        root.right.left = TreeNode(3)
        root.right.right = TreeNode(6)
        self.assertEqual(False, self.solution.isValidBST(root))

    def test_example_3(self):
        root = TreeNode(2)
        root.left = TreeNode(2)
        root.right = TreeNode(2)
        self.assertEqual(False, self.solution.isValidBST(root))

    def test_example_4(self):
        root = TreeNode(5)
        root.left = TreeNode(4)
        root.right = TreeNode(6)
        root.right.left = TreeNode(3)
        root.right.right = TreeNode(7)
        self.assertEqual(False, self.solution.isValidBST(root))

    def test_example_5(self):
        root = TreeNode(3)
        root.left = TreeNode(1)
        root.left.left = TreeNode(0)
        root.left.right = TreeNode(2)
        root.right = TreeNode(5)
        root.right.left = TreeNode(4)
        root.right.right = TreeNode(6)
        self.assertEqual(True, self.solution.isValidBST(root))
