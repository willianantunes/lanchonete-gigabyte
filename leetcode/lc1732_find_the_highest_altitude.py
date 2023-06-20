"""
Solution for LC#1732: Find the Highest Altitude
https://leetcode.com/problems/find-the-highest-altitude/
"""
import unittest


class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        current = highest_altitude = 0
        for net_gain in gain:
            current += net_gain
            highest_altitude = max(highest_altitude, current)
        return highest_altitude


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_example_1(self):
        gain = [-5, 1, 5, 0, -7]
        self.assertEqual(1, self.solution.largestAltitude(gain))

    def test_example_2(self):
        gain = [-4, -3, -2, -1, 4, 3, 2]
        self.assertEqual(0, self.solution.largestAltitude(gain))
