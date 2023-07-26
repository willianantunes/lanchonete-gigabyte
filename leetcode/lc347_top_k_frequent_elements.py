"""
Solution for LC#347: Top K Frequent Elements
https://leetcode.com/problems/top-k-frequent-elements/
"""
import heapq
import unittest

from dataclasses import dataclass
from dataclasses import field


@dataclass(order=True)
class PrioritizedItem:
    value: int = field(compare=False)
    weight: int


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        database = {}
        for num in nums:
            counter = database.get(num, 0) + 1
            database[num] = counter
        frequencies = []
        for key in database:
            counter = database[key]
            item = PrioritizedItem(key, counter)
            heapq.heappush(frequencies, item)
        items = heapq.nlargest(k, frequencies)
        asked_frequencies = []
        for item in items:
            asked_frequencies.append(item.value)
        return asked_frequencies


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_example_1(self):
        nums = [1, 1, 1, 2, 2, 3]
        k = 2
        self.assertEqual([1, 2], self.solution.topKFrequent(nums, k))
