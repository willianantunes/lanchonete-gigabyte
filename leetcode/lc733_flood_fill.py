"""
Solution for LC#733: Flood Fill
https://leetcode.com/problems/flood-fill/description/
"""
import unittest


class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        number_of_rows = len(image)
        number_of_columns = len(image[0])
        color_caught = image[sr][sc]
        image[sr][sc] = color
        cells_4_connected = [(sr, sc)]
        cells_checked = [(sr, sc)]

        def _fill_if_applicable(x, y):
            left, up, right, down = (x, y - 1), (x - 1, y), (x, y + 1), (x + 1, y)
            pixes = [left, up, right, down]
            while pixes:
                cell = pixes.pop()
                if cell not in cells_checked:
                    cells_checked.append(cell)
                    x, y = cell
                    if number_of_rows > x >= 0 and number_of_columns > y >= 0:
                        found_color = image[x][y]
                        if found_color == color_caught:
                            image[x][y] = color
                            cells_4_connected.append((x, y))

        while cells_4_connected:
            row, column = cells_4_connected.pop()
            _fill_if_applicable(row, column)

        return image


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_example_1(self):
        image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
        sr = 1
        sc = 1
        color = 2
        self.assertEqual([[2, 2, 2], [2, 2, 0], [2, 0, 1]], self.solution.floodFill(image, sr, sc, color))

    def test_example_2(self):
        image = [[0, 0, 0], [0, 0, 0]]
        sr = 0
        sc = 0
        color = 0
        self.assertEqual([[0, 0, 0], [0, 0, 0]], self.solution.floodFill(image, sr, sc, color))
