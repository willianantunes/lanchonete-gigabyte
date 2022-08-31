"""
Solution for LC#350: Intersection of Two Arrays II
https://leetcode.com/problems/intersection-of-two-arrays-ii/
"""
import unittest


class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        database_nums1 = {}
        database_nums2 = {}

        for value in nums1:
            occurrences = database_nums1.get(value, 0) + 1
            database_nums1[value] = occurrences

        for value in nums2:
            occurrences = database_nums2.get(value, 0) + 1
            database_nums2[value] = occurrences

        intersection = []

        for entry in database_nums1.keys():
            occurrences_in_nums2 = database_nums2.get(entry)
            if occurrences_in_nums2 is not None:
                occurrences_in_nums1 = database_nums1[entry]
                if occurrences_in_nums1 > occurrences_in_nums2:
                    entries_to_be_inserted = occurrences_in_nums2
                else:
                    entries_to_be_inserted = occurrences_in_nums1
                intersection += [entry for _ in range(entries_to_be_inserted)]

        return intersection


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_example_1(self):
        nums1 = [1, 2, 2, 1]
        nums2 = [2, 2]
        self.assertEqual([2, 2], self.solution.intersect(nums1, nums2))

    def test_example_2(self):
        nums1 = [4, 9, 5]
        nums2 = [9, 4, 9, 8, 4]
        self.assertEqual([4, 9], self.solution.intersect(nums1, nums2))
