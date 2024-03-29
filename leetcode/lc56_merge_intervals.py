"""
Solution for LC#56: Merge Intervals
https://leetcode.com/problems/merge-intervals/
"""
import unittest


class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        result = []
        start = control = None

        def quicksort(array: list) -> list:
            length = len(array)

            less_than_pivot = []
            equal_pivot = []
            greater_than_pivot = []

            if length > 1:
                pivot = array[0]
                for entry in array:
                    if entry[0] < pivot[0]:
                        less_than_pivot.append(entry)
                    elif entry[0] > pivot[0]:
                        greater_than_pivot.append(entry)
                    else:
                        equal_pivot.append(entry)
                return quicksort(less_than_pivot) + equal_pivot + quicksort(greater_than_pivot)
            else:
                return array

        intervals = quicksort(intervals)

        for interval in intervals:
            if start is None:
                start = interval[0]
                control = [interval[1]]
                continue
            interval_start, interval_end = interval[0], interval[1]
            if control[-1] < interval_start:
                result.append([start, control[-1]])
                start = interval[0]
                control = [interval[1]]
            elif control[-1] < interval_end or control[-1] == interval_end:
                control[-1] = interval_end

        if start is not None:
            result.append([start, control[-1]])

        return result


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_example_1(self):
        intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
        self.assertEqual([[1, 6], [8, 10], [15, 18]], self.solution.merge(intervals))

    def test_example_2(self):
        intervals = [[1, 4], [4, 5]]
        self.solution.merge(intervals)
        self.assertEqual([[1, 5]], self.solution.merge(intervals))

    def test_example_3(self):
        intervals = [[1, 4], [1, 5]]
        self.solution.merge(intervals)
        self.assertEqual([[1, 5]], self.solution.merge(intervals))

    def test_example_4(self):
        intervals = [[1, 4], [0, 4]]
        self.solution.merge(intervals)
        self.assertEqual([[0, 4]], self.solution.merge(intervals))

    def test_example_5(self):
        intervals = [[1, 4], [0, 1]]
        self.solution.merge(intervals)
        self.assertEqual([[0, 4]], self.solution.merge(intervals))

    def test_example_6(self):
        intervals = [[1, 4], [2, 3]]
        self.solution.merge(intervals)
        self.assertEqual([[1, 4]], self.solution.merge(intervals))

    def test_example_7(self):
        intervals = [[1, 4], [0, 2], [3, 5]]
        self.solution.merge(intervals)
        # [[0, 2], [1, 4], [3, 5]]
        # [[0, 4], [3, 5]]
        self.assertEqual([[0, 5]], self.solution.merge(intervals))
