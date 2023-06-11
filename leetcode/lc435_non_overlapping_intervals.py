"""
Solution for LC#435: Non-overlapping Intervals
https://leetcode.com/problems/non-overlapping-intervals/
"""
import unittest


def quicksort_first_element(array: list[list[int]]) -> list[list[int]]:
    array_length = len(array)

    if array_length <= 1:
        return array
    else:
        pivot = array[0][0]
        less_than_pivot = []
        greater_than_pivot = []
        equal_pivot = []

        for item in array:
            start = item[0]
            if start < pivot:
                less_than_pivot.append(item)
            elif start > pivot:
                greater_than_pivot.append(item)
            else:
                equal_pivot.append(item)

        return quicksort_first_element(less_than_pivot) + equal_pivot + quicksort_first_element(greater_than_pivot)


class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        number_of_intervals = len(intervals)

        if number_of_intervals == 1:
            return 0

        cache = {}
        intervals = quicksort_first_element(intervals)

        def _count_overlaps(interval_a: int, interval_b: int) -> int:
            cache_key = (interval_a, interval_b)
            cached_result = cache.get(cache_key)
            if cached_result is not None:
                return cached_result
            if interval_b >= number_of_intervals:
                return 0

            a_end = intervals[interval_a][1]
            b_start = intervals[interval_b][0]
            do_not_overlap = b_start >= a_end
            if do_not_overlap:
                counter = _count_overlaps(interval_b, interval_b + 1)
            else:
                counter_b_and_b_plus_1 = _count_overlaps(interval_b, interval_b + 1)
                counter_a_and_b_plus_1 = _count_overlaps(interval_a, interval_b + 1)
                counter = 1 + min(counter_b_and_b_plus_1, counter_a_and_b_plus_1)

            cache[cache_key] = counter

            return counter

        return _count_overlaps(0, 1)


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
