"""
Solution for LC#70: Climbing Stairs
https://leetcode.com/problems/climbing-stairs/
"""
import unittest

from functools import lru_cache


class Solution:
    def climbStairs(self, n: int) -> int:
        @lru_cache
        def _steps_to_reach_top(current_stair) -> int:
            if current_stair == 0:
                return 1
            if current_stair <= 0:
                return 0

            return _steps_to_reach_top(current_stair - 1) + _steps_to_reach_top(current_stair - 2)

        return _steps_to_reach_top(n)


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_example_1(self):
        n = 2
        self.assertEqual(2, self.solution.climbStairs(n))

    def test_example_2(self):
        n = 3
        self.assertEqual(3, self.solution.climbStairs(n))

    def test_example_3(self):
        n = 4
        self.assertEqual(5, self.solution.climbStairs(n))

    def test_example_4(self):
        n = 5
        self.assertEqual(8, self.solution.climbStairs(n))

    def test_example_5(self):
        n = 6
        self.assertEqual(13, self.solution.climbStairs(n))

    def test_example_6(self):
        n = 7
        self.assertEqual(21, self.solution.climbStairs(n))

    def test_example_7(self):
        n = 8
        self.assertEqual(34, self.solution.climbStairs(n))

    def test_example_8(self):
        n = 9
        self.assertEqual(55, self.solution.climbStairs(n))

    def test_example_9(self):
        n = 45
        self.assertEqual(1836311903, self.solution.climbStairs(n))
