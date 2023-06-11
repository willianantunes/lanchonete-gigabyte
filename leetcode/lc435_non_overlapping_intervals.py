"""
Solution for LC#435: Non-overlapping Intervals
https://leetcode.com/problems/non-overlapping-intervals/
"""
import unittest


class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        number_of_intervals = len(intervals)

        if number_of_intervals == 1:
            return 0

        intervals.sort(key=lambda interval: interval[1])
        counter_overlaps = 0
        end_pointer = intervals[0][1]

        for start, end in intervals[1:]:
            overlap = start < end_pointer
            if overlap:
                counter_overlaps += 1
            else:
                end_pointer = end
        return counter_overlaps


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_example_1(self):
        intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
        self.assertEqual(1, self.solution.eraseOverlapIntervals(intervals))

    def test_example_2(self):
        intervals = [[1, 2], [1, 2], [1, 2]]
        self.assertEqual(2, self.solution.eraseOverlapIntervals(intervals))

    def test_example_3(self):
        intervals = [[1, 2], [2, 3]]
        self.assertEqual(0, self.solution.eraseOverlapIntervals(intervals))

    def test_example_4(self):
        intervals = [[0, 2], [1, 2], [2, 3]]
        self.assertEqual(1, self.solution.eraseOverlapIntervals(intervals))

    def test_example_5(self):
        intervals = [[1, 100], [11, 22], [1, 11], [2, 12]]
        self.assertEqual(2, self.solution.eraseOverlapIntervals(intervals))

    def test_example_6(self):
        intervals = [[0, 2], [1, 3], [1, 3], [2, 4], [3, 5], [3, 5], [4, 6]]
        self.assertEqual(4, self.solution.eraseOverlapIntervals(intervals))
