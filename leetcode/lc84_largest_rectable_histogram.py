"""
Solution for LC#84: Largest Rectangle in Histogram
https://leetcode.com/problems/largest-rectangle-in-histogram/
Array / Stack / Monotonic Stack
"""
import unittest

from math import inf


class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        number_of_bars = len(heights)
        if number_of_bars == 1:
            return heights[0]

        max_area = -inf
        stack = []

        for index, height in enumerate(heights):
            start = index
            while stack and height < stack[-1][1]:
                stored_index, stored_height = stack.pop()
                rectangle = stored_height * (index - stored_index)
                max_area = max(max_area, rectangle)
                start = stored_index
            stack.append((start, height))

        for stored_index, stored_height in stack:
            rectangle = stored_height * (number_of_bars - stored_index)
            max_area = max(max_area, rectangle)

        return max_area


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_example_1(self):
        heights = [2, 1, 5, 6, 2, 3]
        self.assertEqual(10, self.solution.largestRectangleArea(heights))

    def test_example_2(self):
        heights = [2, 4]
        self.assertEqual(4, self.solution.largestRectangleArea(heights))

    def test_example_3(self):
        heights = [10, 2, 2, 2, 2, 2, 2]
        self.assertEqual(14, self.solution.largestRectangleArea(heights))

    def test_example_4(self):
        heights = [5, 4, 1, 2]
        self.assertEqual(8, self.solution.largestRectangleArea(heights))

    def test_example_5(self):
        heights = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        self.assertEqual(30, self.solution.largestRectangleArea(heights))

    def test_example_6(self):
        heights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(30, self.solution.largestRectangleArea(heights))
