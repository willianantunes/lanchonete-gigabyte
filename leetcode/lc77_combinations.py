"""
Solution for LC#77: Combinations
https://leetcode.com/problems/combinations/
"""
import unittest


class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        numbers = []

        for value in range(1, n + 1):
            numbers.append(value)

        first_item = numbers[0:k]
        items = [first_item]
        if n == k:
            return items

        total_length = len(first_item)
        end = numbers[-1]
        pointer_position = total_length - 1
        while True:
            item = items[-1].copy()
            last_value = item[-1]
            if last_value != end:
                last_value += 1
                item[pointer_position] = last_value
                items.append(item)
            else:
                while last_value == end:
                    pointer_position -= 1
                    if pointer_position >= 0:
                        base_value = item[pointer_position] + 1
                        for index in range(pointer_position, total_length):
                            item[index] = base_value
                            base_value += 1
                        last_value = item[-1]
                        items.append(item.copy())
                    else:
                        return items
                pointer_position = total_length - 1


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_example_1(self):
        n = 4
        k = 2
        self.assertEqual(
            [
                [1, 2],
                [1, 3],
                [1, 4],
                [2, 3],
                [2, 4],
                [3, 4],
            ],
            self.solution.combine(n, k),
        )

    def test_example_2(self):
        n = 1
        k = 1
        self.assertEqual([[1]], self.solution.combine(n, k))

    def test_example_3(self):
        n = 4
        k = 4
        self.assertEqual([[1, 2, 3, 4]], self.solution.combine(n, k))

    def test_example_4(self):
        n = 8
        k = 2
        self.assertEqual(
            [
                [1, 2],
                [1, 3],
                [1, 4],
                [1, 5],
                [1, 6],
                [1, 7],
                [1, 8],
                [2, 3],
                [2, 4],
                [2, 5],
                [2, 6],
                [2, 7],
                [2, 8],
                [3, 4],
                [3, 5],
                [3, 6],
                [3, 7],
                [3, 8],
                [4, 5],
                [4, 6],
                [4, 7],
                [4, 8],
                [5, 6],
                [5, 7],
                [5, 8],
                [6, 7],
                [6, 8],
                [7, 8],
            ],
            self.solution.combine(n, k),
        )

    def test_example_5(self):
        n = 8
        k = 4
        self.assertEqual(
            [
                [1, 2, 3, 4],
                [1, 2, 3, 5],
                [1, 2, 3, 6],
                [1, 2, 3, 7],
                [1, 2, 3, 8],
                [1, 2, 4, 5],
                [1, 2, 4, 6],
                [1, 2, 4, 7],
                [1, 2, 4, 8],
                [1, 2, 5, 6],
                [1, 2, 5, 7],
                [1, 2, 5, 8],
                [1, 2, 6, 7],
                [1, 2, 6, 8],
                [1, 2, 7, 8],
                [1, 3, 4, 5],
                [1, 3, 4, 6],
                [1, 3, 4, 7],
                [1, 3, 4, 8],
                [1, 3, 5, 6],
                [1, 3, 5, 7],
                [1, 3, 5, 8],
                [1, 3, 6, 7],
                [1, 3, 6, 8],
                [1, 3, 7, 8],
                [1, 4, 5, 6],
                [1, 4, 5, 7],
                [1, 4, 5, 8],
                [1, 4, 6, 7],
                [1, 4, 6, 8],
                [1, 4, 7, 8],
                [1, 5, 6, 7],
                [1, 5, 6, 8],
                [1, 5, 7, 8],
                [1, 6, 7, 8],
                [2, 3, 4, 5],
                [2, 3, 4, 6],
                [2, 3, 4, 7],
                [2, 3, 4, 8],
                [2, 3, 5, 6],
                [2, 3, 5, 7],
                [2, 3, 5, 8],
                [2, 3, 6, 7],
                [2, 3, 6, 8],
                [2, 3, 7, 8],
                [2, 4, 5, 6],
                [2, 4, 5, 7],
                [2, 4, 5, 8],
                [2, 4, 6, 7],
                [2, 4, 6, 8],
                [2, 4, 7, 8],
                [2, 5, 6, 7],
                [2, 5, 6, 8],
                [2, 5, 7, 8],
                [2, 6, 7, 8],
                [3, 4, 5, 6],
                [3, 4, 5, 7],
                [3, 4, 5, 8],
                [3, 4, 6, 7],
                [3, 4, 6, 8],
                [3, 4, 7, 8],
                [3, 5, 6, 7],
                [3, 5, 6, 8],
                [3, 5, 7, 8],
                [3, 6, 7, 8],
                [4, 5, 6, 7],
                [4, 5, 6, 8],
                [4, 5, 7, 8],
                [4, 6, 7, 8],
                [5, 6, 7, 8],
            ],
            self.solution.combine(n, k),
        )

    def test_example_6(self):
        n = 8
        k = 3
        self.assertEqual(
            [
                [1, 2, 3],
                [1, 2, 4],
                [1, 2, 5],
                [1, 2, 6],
                [1, 2, 7],
                [1, 2, 8],
                [1, 3, 4],
                [1, 3, 5],
                [1, 3, 6],
                [1, 3, 7],
                [1, 3, 8],
                [1, 4, 5],
                [1, 4, 6],
                [1, 4, 7],
                [1, 4, 8],
                [1, 5, 6],
                [1, 5, 7],
                [1, 5, 8],
                [1, 6, 7],
                [1, 6, 8],
                [1, 7, 8],
                [2, 3, 4],
                [2, 3, 5],
                [2, 3, 6],
                [2, 3, 7],
                [2, 3, 8],
                [2, 4, 5],
                [2, 4, 6],
                [2, 4, 7],
                [2, 4, 8],
                [2, 5, 6],
                [2, 5, 7],
                [2, 5, 8],
                [2, 6, 7],
                [2, 6, 8],
                [2, 7, 8],
                [3, 4, 5],
                [3, 4, 6],
                [3, 4, 7],
                [3, 4, 8],
                [3, 5, 6],
                [3, 5, 7],
                [3, 5, 8],
                [3, 6, 7],
                [3, 6, 8],
                [3, 7, 8],
                [4, 5, 6],
                [4, 5, 7],
                [4, 5, 8],
                [4, 6, 7],
                [4, 6, 8],
                [4, 7, 8],
                [5, 6, 7],
                [5, 6, 8],
                [5, 7, 8],
                [6, 7, 8],
            ],
            self.solution.combine(n, k),
        )
