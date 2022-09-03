"""
Solution for LC#101: Symmetric Tree
https://leetcode.com/problems/symmetric-tree/
"""
import unittest

from collections import Counter


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: TreeNode | None) -> bool:
        if not root or (root and not root.left and not root.right):
            return True
        if (root.left and not root.right) or (root.right and not root.left):
            return False

        counter = Counter()
        left_side = {}
        right_side = {}

        def _traversal(node: TreeNode, store: dict):
            store_key = counter["level"]
            values = store.get(store_key, [])
            values.append(node.val if node else None)
            store[store_key] = values

            if node:
                counter["level"] += 1
                _traversal(node.left, store)
                _traversal(node.right, store)
                counter["maximum_depth"] = max(counter["level"], counter["maximum_depth"])
                counter["level"] -= 1

        _traversal(root.left, left_side)
        _traversal(root.right, right_side)
        depth_considering_root = counter["maximum_depth"] + 1
        level = 0

        while level < depth_considering_root:
            if level == 0:
                if left_side[level][0] != right_side[level][0]:
                    return False
                level += 1
            else:
                left_side_partition = left_side[level]
                right_side_partition = right_side[level]
                number_of_nodes_current_level = len(left_side_partition)
                right_pointer = number_of_nodes_current_level - 1

                for left_pointer in range(number_of_nodes_current_level):
                    if left_side_partition[left_pointer] != right_side_partition[right_pointer]:
                        return False
                    right_pointer -= 1

                level += 1

        return True


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_example_1(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(3)
        root.left.right = TreeNode(4)
        root.right = TreeNode(2)
        root.right.right = TreeNode(3)
        root.right.left = TreeNode(4)
        self.assertEqual(True, self.solution.isSymmetric(root))

    def test_example_2(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.right = TreeNode(3)
        root.right = TreeNode(2)
        root.right.right = TreeNode(3)
        self.assertEqual(False, self.solution.isSymmetric(root))

    def test_example_3(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        self.assertEqual(False, self.solution.isSymmetric(root))

    def test_example_4(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(2)
        self.assertEqual(True, self.solution.isSymmetric(root))

    def test_example_5(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(2)
        root.right = TreeNode(2)
        root.right.right = TreeNode(2)
        root.right.left = TreeNode(2)
        self.assertEqual(False, self.solution.isSymmetric(root))

    def test_example_6(self):
        root = TreeNode(1)
        self.assertEqual(True, self.solution.isSymmetric(root))

    def test_example_7(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.right = TreeNode(3)
        root.right = TreeNode(2)
        root.right.left = TreeNode(3)
        self.assertEqual(True, self.solution.isSymmetric(root))

    def test_example_8(self):
        root = TreeNode(2)
        root.left = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.left.right.left = TreeNode(8)
        root.left.right.right = TreeNode(9)
        root.right = TreeNode(3)
        root.right.left = TreeNode(5)
        root.right.right = TreeNode(4)
        root.right.left.left = TreeNode(9)
        root.right.left.right = TreeNode(8)
        self.assertEqual(True, self.solution.isSymmetric(root))
