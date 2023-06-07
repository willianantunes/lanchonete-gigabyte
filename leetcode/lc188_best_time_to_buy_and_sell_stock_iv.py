"""
Solution for LC#188: Best Time to Buy and Sell Stock IV
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/
"""
import unittest


class Solution:
    def maxProfit(self, k: int, prices: list[int]) -> int:
        number_of_days = len(prices)

        def _evaluate(allowed_transactions: int, profit: int, day: int, pending_transaction, lowest_price: int | None):
            if allowed_transactions <= 0 or day >= number_of_days:
                return profit + pending_transaction

            stock_price = prices[day]
            if lowest_price is not None:
                if stock_price < lowest_price:
                    lowest_price = stock_price
                    if pending_transaction:
                        profit += pending_transaction
                        pending_transaction = 0
                        allowed_transactions -= 1
                else:
                    pending_transaction += stock_price - lowest_price
                    lowest_price = stock_price
            else:
                lowest_price = stock_price

            return _evaluate(allowed_transactions, profit, day + 1, pending_transaction, lowest_price)

        return _evaluate(k, 0, 1, 0, prices[0])


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
