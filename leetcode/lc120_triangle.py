"""
Solution for LC#120: Triangle
https://leetcode.com/problems/triangle/
"""
import heapq
import unittest


class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        pyramid_size = len(triangle)
        for level in range(1, pyramid_size):
            cells = triangle[level]
            number_of_cells = len(cells)
            for index, value in enumerate(cells):
                if index == 0:
                    for i, v in enumerate(cells):
                        cells[i] = [v, []]
                    current_trial_value = cells[index][0] + triangle[level - 1][index]
                elif index == number_of_cells - 1:
                    current_trial_value = cells[index][0] + triangle[level - 1][index - 1]
                else:
                    upper_left = cells[index][0] + triangle[level - 1][index - 1]
                    upper_right = cells[index][0] + triangle[level - 1][index]
                    current_trial_value = upper_left if upper_left < upper_right else upper_right
                heapq.heappush(cells[index][1], current_trial_value)
            for i, v in enumerate(cells):
                cells[i] = heapq.nsmallest(1, cells[i][1])[0]
        return min(triangle[pyramid_size - 1])


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_example_1(self):
        triangle = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
        self.assertEqual(11, self.solution.minimumTotal(triangle))

    def test_example_2(self):
        triangle = [[-10]]
        self.assertEqual(-10, self.solution.minimumTotal(triangle))

    def test_example_3(self):
        triangle = [[-1], [2, 3], [1, -1, -3]]
        self.assertEqual(-1, self.solution.minimumTotal(triangle))

    def test_example_4(self):
        triangle = [[2], [3, 4], [6, 5, 9], [4, 4, 8, 0]]
        self.assertEqual(14, self.solution.minimumTotal(triangle))
