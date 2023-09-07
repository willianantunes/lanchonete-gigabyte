"""
Solution for LC#739: Daily Temperatures
https://leetcode.com/problems/daily-temperatures/
Array / Stack / Monotonic Stack
"""
import unittest


class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        stack = []
        total_of_days = len(temperatures)
        answer = [0] * total_of_days

        for day in range(total_of_days):
            current_temperature = temperatures[day]
            while stack and current_temperature > temperatures[stack[-1]]:
                target_day = stack.pop()
                answer[target_day] = day - target_day
            stack.append(day)

        return answer


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_example_1(self):
        temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
        self.assertEqual([1, 1, 4, 2, 1, 1, 0, 0], self.solution.dailyTemperatures(temperatures))

    def test_example_2(self):
        temperatures = [30, 40, 50, 60]
        self.assertEqual([1, 1, 1, 0], self.solution.dailyTemperatures(temperatures))

    def test_example_3(self):
        temperatures = [30, 60, 90]
        self.assertEqual([1, 1, 0], self.solution.dailyTemperatures(temperatures))
