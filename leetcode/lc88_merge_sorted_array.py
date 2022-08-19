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
        if (m == 1 and n == 0) or (m > 1 and n == 0):
            return
        if m == 0 and n == 1:
            nums1[0] = nums2[0]
            return
        if m == 0 and n > 1:
            for index, value in enumerate(nums2):
                nums1[index] = value
            return

        number_of_entries = m + n
        pointer_left, pointer_right = 0, 0

        while pointer_left < number_of_entries:
            current_nums1_value = nums1[pointer_left]
            current_nums2_value = nums2[pointer_right]

            if pointer_left >= m:
                nums1[pointer_left] = current_nums2_value
                pointer_right += 1
            elif current_nums1_value > current_nums2_value:
                nums1[pointer_left] = current_nums2_value
                nums2[pointer_right] = current_nums1_value
                for sorting_pointer_limit in range(n - 1, 0, -1):
                    for sorting_pointer_left in range(sorting_pointer_limit):
                        sorting_pointer_right = sorting_pointer_left + 1
                        if nums2[sorting_pointer_left] > nums2[sorting_pointer_right]:
                            nums2[sorting_pointer_left], nums2[sorting_pointer_right] = (
                                nums2[sorting_pointer_right],
                                nums2[sorting_pointer_left],
                            )

            pointer_left += 1


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
