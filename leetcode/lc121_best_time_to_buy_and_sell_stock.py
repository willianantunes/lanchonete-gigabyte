"""
Solution for LC#121: Best Time to Buy and Sell Stock
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
"""
import unittest


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_profit = 0
        lowest_price = prices[0]

        for index in range(1, len(prices)):
            stock_price = prices[index]
            if stock_price < lowest_price:
                lowest_price = stock_price
            else:
                max_profit = max(max_profit, stock_price - lowest_price)

        return max_profit


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_example_1(self):
        prices = [7, 1, 5, 3, 6, 4]
        self.assertEqual(5, self.solution.maxProfit(prices))

    def test_example_2(self):
        prices = [7, 6, 4, 3, 1]
        self.assertEqual(0, self.solution.maxProfit(prices))
