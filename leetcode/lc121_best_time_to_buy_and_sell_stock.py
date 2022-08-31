"""
Solution for LC#121: Best Time to Buy and Sell Stock
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
"""
import unittest


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        best_profit = 0
        best_buy_index = best_sell_index = 0

        for current_index, value in enumerate(prices):
            best_buy = prices[best_buy_index]
            best_sell = prices[best_sell_index]

            if best_buy > value:
                best_buy_index = current_index
                best_sell_index = current_index
            elif best_sell < value:
                best_sell_index = current_index
                best_sell = value
                profit = best_sell - best_buy
                best_profit = max(profit, best_profit)

        return best_profit


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_example_1(self):
        prices = [7, 1, 5, 3, 6, 4]
        self.assertEqual(5, self.solution.maxProfit(prices))

    def test_example_2(self):
        prices = [7, 6, 4, 3, 1]
        self.assertEqual(0, self.solution.maxProfit(prices))
