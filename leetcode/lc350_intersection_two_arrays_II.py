"""
Solution for LC#350: Intersection of Two Arrays II
https://leetcode.com/problems/intersection-of-two-arrays-ii/
"""
import unittest


class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        database_nums1 = {}
        database_nums2 = {}

        for item in nums1:
            counter = database_nums1.get(item, 0) + 1
            database_nums1[item] = counter

        for item in nums2:
            counter = database_nums2.get(item, 0) + 1
            database_nums2[item] = counter

        intersect = []
        for number in database_nums1:
            occurrences = database_nums1[number]
            occurrences_from_nums2 = database_nums2.get(number)
            if occurrences_from_nums2 is not None:
                times = min(occurrences, occurrences_from_nums2)
                intersect += [number for _ in range(times)]

        return intersect


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
