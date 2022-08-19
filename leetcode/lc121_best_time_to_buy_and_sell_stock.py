"""
Solution for LC#121: Best Time to Buy and Sell Stock
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
"""
import unittest

from dataclasses import dataclass


@dataclass(frozen=True)
class ProfitOpportunity:
    best_buy_index: int
    price_buy: int
    best_sell_index: int
    price_sell: int
    profit: int


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        best_buy_index, price_buy = 0, 0
        best_sell_index, price_sell = 0, 0
        opportunities = []

        for index, current_stock_value in enumerate(prices):
            if index == 0:
                price_buy, price_sell = current_stock_value, current_stock_value
                continue

            is_good_opportunity_to_sell = current_stock_value > price_sell
            is_good_opportunity_to_buy = current_stock_value < price_buy

            if is_good_opportunity_to_sell:
                best_sell_index, price_sell = index, current_stock_value
            elif is_good_opportunity_to_buy:
                best_sell_index, price_sell = index, current_stock_value
                best_buy_index, price_buy = index, current_stock_value

            profit = price_sell - price_buy
            if profit > 0:
                opportunity = ProfitOpportunity(best_buy_index, price_buy, best_sell_index, price_sell, profit)
                opportunities.append(opportunity)

        maximum_profit = 0

        for opportunity in opportunities:
            if opportunity.profit > maximum_profit:
                maximum_profit = opportunity.profit

        return maximum_profit


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_example_1(self):
        prices = [7, 1, 5, 3, 6, 4]
        self.assertEqual(5, self.solution.maxProfit(prices))

    def test_example_2(self):
        prices = [7, 6, 4, 3, 1]
        self.assertEqual(0, self.solution.maxProfit(prices))
