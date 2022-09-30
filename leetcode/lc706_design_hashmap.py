"""
Solution for LC#706: Design HashMap
https://leetcode.com/problems/design-hashmap/
"""
import unittest


class MyHashMap:
    def __init__(self):
        self.store = [-1] * 10**7

    def put(self, key: int, value: int) -> None:
        self.store[key] = value

    def get(self, key: int) -> int:
        return self.store[key]

    def remove(self, key: int) -> None:
        self.store[key] = -1


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = MyHashMap()

    def test_example_1(self):
        self.solution.put(1000000, 1)
        self.solution.put(1, 1)
        self.solution.put(1, 1)
        self.solution.put(2, 2)
        self.solution.get(1)
        self.solution.get(3)
        self.solution.put(2, 1)
        self.solution.get(2)
        self.solution.remove(2)
        self.solution.get(2)
