"""
Solution for LC#88: Merge Sorted Array
https://leetcode.com/problems/merge-sorted-array/
"""
import unittest


class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m > 0 and n == 0:
            return
        if m == 0 and n > 0:
            for index, value in enumerate(nums2):
                nums1[index] = value
            return
        pointer_nums1 = 0
        pointer_nums2 = 0
        total = m + n

        while pointer_nums1 < total:
            current_nums1_value = nums1[pointer_nums1]
            current_nums2_value = nums2[pointer_nums2]

            if pointer_nums1 < m:
                if current_nums1_value <= current_nums2_value:
                    pointer_nums1 += 1
                else:
                    nums1[pointer_nums1] = current_nums2_value
                    nums2[pointer_nums2] = current_nums1_value
                    pointer_nums1 += 1
            else:
                nums1[pointer_nums1] = current_nums2_value
                nums2[pointer_nums2] = 0
                pointer_nums1 = 0
                pointer_nums2 += 1
                m += 1
                if m == total:
                    break


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_example_1(self):
        nums1 = [1, 2, 3, 0, 0, 0]
        m = 3
        nums2 = [2, 5, 6]
        n = 3
        self.solution.merge(nums1, m, nums2, n)
        self.assertEqual([1, 2, 2, 3, 5, 6], nums1)

    def test_example_2(self):
        nums1 = [1]
        m = 1
        nums2 = []
        n = 0
        self.solution.merge(nums1, m, nums2, n)
        self.assertEqual([1], nums1)

    def test_example_3(self):
        nums1 = [0]
        m = 0
        nums2 = [1]
        n = 1
        self.solution.merge(nums1, m, nums2, n)
        self.assertEqual([1], nums1)

    def test_example_4(self):
        nums1 = [4, 5, 6, 0, 0, 0]
        m = 3
        nums2 = [1, 2, 3]
        n = 3
        self.solution.merge(nums1, m, nums2, n)
        self.assertEqual([1, 2, 3, 4, 5, 6], nums1)

    def test_example_5(self):
        nums1 = [4, 0, 0, 0, 0, 0]
        m = 1
        nums2 = [1, 2, 3, 5, 6]
        n = 5
        self.solution.merge(nums1, m, nums2, n)
        self.assertEqual([1, 2, 3, 4, 5, 6], nums1)
