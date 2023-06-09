"""
Solution for LC#188: Best Time to Buy and Sell Stock IV
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/
"""
import unittest


class Solution:
    def maxProfit(self, k: int, prices: list[int]) -> int:
        number_of_days = len(prices)
        # Debug counter value and check the huge optimization by yourself
        cache = {"counter": 0}

        def _evaluate(allowed_transactions: int, day: int, is_bought: bool):
            if allowed_transactions == 0 or day >= number_of_days:
                return 0
            known_result = cache.get(allowed_transactions, {}).get(day, {}).get(is_bought)
            if known_result is not None:
                return known_result

            when_bought = when_sold = 0
            next_day = day + 1
            if is_bought:
                when_bought = prices[day] + _evaluate(allowed_transactions - 1, next_day, False)
            else:
                when_sold = -prices[day] + _evaluate(allowed_transactions, next_day, True)
            when_stay_still = _evaluate(allowed_transactions, next_day, is_bought)

            cache["counter"] += 1
            known_result = max(when_bought, when_sold, when_stay_still)
            if not cache.get(allowed_transactions):
                cache[allowed_transactions] = {}
            if not cache[allowed_transactions].get(day):
                cache[allowed_transactions][day] = {}
            cache[allowed_transactions][day][is_bought] = known_result
            return known_result

        # O(allowed_transactions * day * 2) => O(allowed_transactions * day)
        return _evaluate(k, 0, False)


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_example_1(self):
        k = 2
        prices = [2, 4, 1]
        self.assertEqual(2, self.solution.maxProfit(k, prices))

    def test_example_2(self):
        k = 2
        prices = [3, 2, 6, 5, 0, 3]
        self.assertEqual(7, self.solution.maxProfit(k, prices))

    def test_example_3(self):
        k = 2
        prices = [10, 1, 8, 11, 8, 9]
        self.assertEqual(11, self.solution.maxProfit(k, prices))

    def test_example_4(self):
        k = 2
        prices = [3, 3, 5, 0, 0, 3, 1, 4]
        self.assertEqual(6, self.solution.maxProfit(k, prices))

    def test_example_5(self):
        k = 2
        prices = [1, 6, 0, 0, 20, 2, 3, 4, 5]
        self.assertEqual(25, self.solution.maxProfit(k, prices))

    def test_example_6(self):
        k = 2
        prices = [3, 5, 0, 0, 5, 1, 10]
        # (3, 5) = 2
        # (0, 5) = 5
        # (1, 10) = 9
        self.assertEqual(14, self.solution.maxProfit(k, prices))

    def test_example_7(self):
        k = 3
        prices = [3, 5, 0, 0, 5, 1, 10]
        # (3, 5) = 2
        # (0, 5) = 5
        # (1, 10) = 9
        self.assertEqual(16, self.solution.maxProfit(k, prices))

    def test_example_8(self):
        k = 2
        prices = [1, 2, 4, 2, 5, 7, 2, 4, 9, 0]
        # (1, 7) = 6
        # (2, 9) = 7
        self.assertEqual(13, self.solution.maxProfit(k, prices))

    def test_example_9(self):
        k = 3
        prices = [1, 2, 4, 2, 5, 7, 2, 4, 9, 0]
        # (1, 4) = 3
        # (2, 7) = 5
        # (2, 9) = 7
        self.assertEqual(15, self.solution.maxProfit(k, prices))

    def test_example_10(self):
        k = 2
        prices = [1]
        self.assertEqual(0, self.solution.maxProfit(k, prices))

    def test_example_11(self):
        k = 2
        prices = [1, 2, 4, 2, 5, 7, 2, 4, 9, 0, 9]
        # (1, 9) = 8
        # (0, 9) = 9
        self.assertEqual(17, self.solution.maxProfit(k, prices))

    def test_example_12(self):
        k = 2
        prices = [6, 5, 4, 8, 6, 8, 7, 8, 9, 4, 5]
        # (4, 8) = 4
        # (6, 9) = 3
        # Without cache properly implemented the counter has 561
        # With proper cache: 38
        self.assertEqual(7, self.solution.maxProfit(k, prices))
