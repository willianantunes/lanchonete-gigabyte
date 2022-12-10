import unittest


def binary_search(array: list[int], target_value: int) -> bool:
    array_length = len(array)
    start = 0
    end = array_length - 1

    while start <= end:
        middle = (start + end) // 2
        value = array[middle]
        if value == target_value:
            return True
        elif target_value < value:
            end = middle - 1
        else:
            start = middle + 1

    return False


class TestBinarySearch(unittest.TestCase):
    def test_example_1(self):
        array = [9, 8, 7, 3, 2, 1, 6, 5, 4, 3, 2, 6, 4, 3]
        array.sort()
        self.assertTrue(binary_search(array, 9))
        self.assertTrue(binary_search(array, 1))
        self.assertFalse(binary_search(array, 10))
        self.assertFalse(binary_search(array, 0))
        self.assertFalse(binary_search(array, -50))

    def test_example_2(self):
        array = [2, 2, 2, 2, 2, 1, 6, 5, 4, 3, 2, 6, -1, 3]
        array.sort()
        self.assertTrue(binary_search(array, 2))
        self.assertTrue(binary_search(array, -1))
        self.assertTrue(binary_search(array, 6))
        self.assertFalse(binary_search(array, -2))
        self.assertFalse(binary_search(array, 7))

    def test_example_3(self):
        array = list(range(0, 12))
        self.assertTrue(binary_search(array, 4))
        self.assertFalse(binary_search(array, 1000))
        self.assertFalse(binary_search(array, -1))
