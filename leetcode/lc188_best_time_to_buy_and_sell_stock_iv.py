"""
Solution for LC#188: Best Time to Buy and Sell Stock IV
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/
"""
import heapq
import unittest


class Solution:
    def maxProfit(self, k: int, prices: list[int]) -> int:
        number_of_days = len(prices)

        def _evaluate(profits: list, day: int, pending_transaction, lowest_price: int | None):
            if day >= number_of_days:
                if pending_transaction:
                    heapq.heappush(profits, pending_transaction)
                return sum(heapq.nlargest(k, profits))

            stock_price = prices[day]
            if lowest_price is not None:
                if stock_price < lowest_price:
                    lowest_price = stock_price
                    if pending_transaction:
                        heapq.heappush(profits, pending_transaction)
                        pending_transaction = 0
                else:
                    pending_transaction += stock_price - lowest_price
                    lowest_price = stock_price
            else:
                lowest_price = stock_price

            return _evaluate(profits, day + 1, pending_transaction, lowest_price)

        return _evaluate([], 1, 0, prices[0])


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
        self.assertEqual(14, self.solution.maxProfit(k, prices))

    def test_example_7(self):
        k = 2
        prices = [1, 2, 4, 2, 5, 7, 2, 4, 9, 0]
        self.assertEqual(13, self.solution.maxProfit(k, prices))
