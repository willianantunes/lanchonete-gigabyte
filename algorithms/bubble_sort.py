import unittest


def bubble_sort(array: list):
    array_length = len(array)
    for left in range(array_length):
        for right in range(left + 1, array_length):
            left_value = array[left]
            right_value = array[right]
            if left_value > right_value:
                array[left], array[right] = array[right], array[left]


class TestBubbleSort(unittest.TestCase):
    def test_0(self):
        array, expected = [8, 7, 6, 1, 0, 9, 2], [8, 7, 6, 1, 0, 9, 2]
        bubble_sort(array)
        expected.sort()
        self.assertEqual(expected, array)

    def test_1(self):
        array, expected = [6, 1, 3, 110, 123, 2, 5, 0], [6, 1, 3, 110, 123, 2, 5, 0]
        bubble_sort(array)
        expected.sort()
        self.assertEqual(expected, array)

    def test_2(self):
        target_array, expected = [1, 5, 4, 2, 7, 6, 4, 2, 12312, 54, 7, 31, 1], [
            1,
            5,
            4,
            2,
            7,
            6,
            4,
            2,
            12312,
            54,
            7,
            31,
            1,
        ]
        bubble_sort(target_array)
        expected.sort()
        self.assertEqual(expected, target_array)

    def test_3(self):
        target_array, array = [9, 8, 7, 3, 2, 1, 6, 5, 4, 3, 2, 6, 4, 3], [9, 8, 7, 3, 2, 1, 6, 5, 4, 3, 2, 6, 4, 3]
        bubble_sort(target_array)
        array.sort()
        self.assertEqual(array, target_array)

    def test_4(self):
        target_array, array = [2, 2, 2, 2, 2, 1, 6, 5, 4, 3, 2, 6, -1, 3], [2, 2, 2, 2, 2, 1, 6, 5, 4, 3, 2, 6, -1, 3]
        interactions = bubble_sort(target_array)
        array.sort()
        self.assertEqual(array, target_array)

    def test_5(self):
        target_array, array = list(range(6, -1, -1)), list(range(6, -1, -1))
        bubble_sort(target_array)
        array.sort()
        self.assertEqual(array, target_array)
