"""
Solution for LC#188: Best Time to Buy and Sell Stock IV
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/
"""
import heapq
import unittest


class Solution:
    def maxProfit(self, k: int, prices: list[int]) -> int:
        number_of_days = len(prices)

        def _extract_profits(transactions: list[tuple], split_when_possible: bool) -> list[int]:
            profits = []
            base = previous = transactions[0]
            for index in range(1, len(transactions)):
                target = transactions[index]
                low_price, stock_price = target
                might_bind = low_price >= previous[0] and previous[1] < stock_price
                can_split = previous[1] > low_price or previous[1] < low_price
                if split_when_possible:
                    if might_bind and can_split:
                        heapq.heappush(profits, previous[1] - base[0])
                        base = previous = target
                    elif might_bind:
                        previous = target
                    else:
                        heapq.heappush(profits, previous[1] - base[0])
                        base = previous = target
                elif might_bind:
                    previous = target
                else:
                    heapq.heappush(profits, previous[1] - base[0])
                    base = previous = target
            heapq.heappush(profits, previous[1] - base[0])
            return profits

        def _evaluate(possible_profits: list, day: int, low_price: int, transactions: list[tuple]):
            if day >= number_of_days:
                result = 0
                if transactions:
                    profits_with_merge = _extract_profits(transactions, split_when_possible=False)
                    profits_with_split = _extract_profits(transactions, split_when_possible=True)
                    result = max(sum(heapq.nlargest(k, profits_with_merge)), sum(heapq.nlargest(k, profits_with_split)))
                return result

            stock_price = prices[day]
            if low_price is not None:
                if stock_price <= low_price:
                    low_price = stock_price
                else:
                    transactions.append((low_price, stock_price))
                    low_price = stock_price
            else:
                low_price = stock_price

            return _evaluate(possible_profits, day + 1, low_price, transactions)

        return _evaluate([], 1, prices[0], [])


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
