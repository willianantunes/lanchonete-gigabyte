"""
Solution for LC#1046: Last Stone Weight
https://leetcode.com/problems/last-stone-weight/
"""
import heapq
import unittest


class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        heaviest_stones_to_retrieve = 2
        stones_with_weights = []
        for stone_weight in stones:
            heapq.heappush(stones_with_weights, stone_weight)
        while len(heaviest_two_stones := heapq.nlargest(heaviest_stones_to_retrieve, stones_with_weights)) == 2:
            stone_1_weight = heaviest_two_stones[0]
            stone_2_weight = heaviest_two_stones[1]
            stones_with_weights.remove(stone_1_weight)
            stones_with_weights.remove(stone_2_weight)
            must_combine_stones = stone_1_weight != stone_2_weight
            if must_combine_stones:
                if stone_1_weight <= stone_2_weight:
                    new_weight = stone_2_weight - stone_1_weight
                    heapq.heappush(stones_with_weights, new_weight)
                else:
                    new_weight = stone_1_weight - stone_2_weight
                    heapq.heappush(stones_with_weights, new_weight)
        else:
            return heaviest_two_stones[0] if heaviest_two_stones else 0


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(1, self.solution.lastStoneWeight([2, 7, 4, 1, 8, 1]))

    def test_example_2(self):
        self.assertEqual(1, self.solution.lastStoneWeight([1]))

    def test_example_3(self):
        self.assertEqual(None, self.solution.lastStoneWeight([2, 2]))
