import unittest

from random import randint


def quicksort_recursion(array: list[int]) -> list:
    array_length = len(array)

    if array_length > 1:
        pivot = array[0]
        less_than_pivot = []
        greater_than_pivot = []
        equal_pivot = []

        for item in array:
            if item < pivot:
                less_than_pivot.append(item)
            elif item > pivot:
                greater_than_pivot.append(item)
            else:
                equal_pivot.append(item)

        return quicksort_recursion(less_than_pivot) + equal_pivot + quicksort_recursion(greater_than_pivot)

    return array


def quicksort_recursion_inplace_1(array: list[int]):
    array_length = len(array)
    if array_length == 1:
        return

    def _partition(start: int, end: int, target_array: list[int]) -> int:
        pivot_index = randint(start, end)
        pivot_value = target_array[pivot_index]

        # Swap the pivot with the end of the array
        target_array[pivot_index], target_array[end] = target_array[end], target_array[pivot_index]

        pointer_i = start
        pointer_j = end - 1

        while pointer_i <= pointer_j:
            while pointer_i <= pointer_j and target_array[pointer_i] <= pivot_value:
                pointer_i += 1
            while pointer_j >= pointer_i and target_array[pointer_j] >= pivot_value:
                pointer_j -= 1
            if pointer_i < pointer_j:
                target_array[pointer_i], target_array[pointer_j] = target_array[pointer_j], target_array[pointer_i]

        # place pivot back in the right place
        # all values < pivot are to its left and
        # all values > pivot are to its right
        target_array[end], target_array[pointer_i] = target_array[pointer_i], pivot_value

        return pointer_i

    def _quicksort(start, end, target_array):
        if start >= end:
            return

        partition_index = _partition(start, end, target_array)
        _quicksort(start, partition_index - 1, array)
        _quicksort(partition_index + 1, end, array)

    _quicksort(0, array_length - 1, array)


def quicksort_recursion_inplace_2(array: list[int]):
    array_length = len(array)
    if array_length == 1:
        return

    def _partition(start, end) -> int:
        pivot_value = array[end]

        greater_than_p_index = start - 1

        for current_index in range(start, end):
            if array[current_index] < pivot_value:
                greater_than_p_index += 1
                array[greater_than_p_index], array[current_index] = array[current_index], array[greater_than_p_index]

        greater_than_p_index += 1
        array[greater_than_p_index], array[end] = array[end], array[greater_than_p_index]
        return greater_than_p_index

    def _quicksort(start, end):
        if start >= end:
            return

        pivot_index = _partition(start, end)
        _quicksort(start, pivot_index - 1)
        _quicksort(pivot_index + 1, end)

    _quicksort(0, array_length - 1)


class TestQuicksortInPlace1(unittest.TestCase):
    def test_example_0(self):
        target_array, array = [8, 7, 6, 1, 0, 9, 2], [8, 7, 6, 1, 0, 9, 2]
        quicksort_recursion_inplace_1(target_array)
        array.sort()
        self.assertEqual(array, target_array)

    def test_example_1(self):
        target_array, array = [1, 5, 4, 2, 7, 6, 4, 2, 12312, 54, 7, 31, 1], [
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
        quicksort_recursion_inplace_1(target_array)
        array.sort()
        self.assertEqual(array, target_array)

    def test_example_2(self):
        target_array, array = [9, 8, 7, 3, 2, 1, 6, 5, 4, 3, 2, 6, 4, 3], [9, 8, 7, 3, 2, 1, 6, 5, 4, 3, 2, 6, 4, 3]
        quicksort_recursion_inplace_1(array)
        target_array.sort()
        self.assertEqual(target_array, target_array)

    def test_example_3(self):
        array, expected = [6, 1, 3, 110, 123, 2, 5, 0], [6, 1, 3, 110, 123, 2, 5, 0]
        quicksort_recursion_inplace_1(array)
        expected.sort()
        self.assertEqual(expected, array)


class TestQuicksortInPlace2(unittest.TestCase):
    def test_example_0(self):
        target_array, array = [8, 7, 6, 1, 0, 9, 2], [8, 7, 6, 1, 0, 9, 2]
        quicksort_recursion_inplace_2(target_array)
        array.sort()
        self.assertEqual(array, target_array)

    def test_example_1(self):
        target_array, array = [1, 5, 4, 2, 7, 6, 4, 2, 12312, 54, 7, 31, 1], [
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
        quicksort_recursion_inplace_2(target_array)
        array.sort()
        self.assertEqual(array, target_array)

    def test_example_2(self):
        target_array, array = [9, 8, 7, 3, 2, 1, 6, 5, 4, 3, 2, 6, 4, 3], [9, 8, 7, 3, 2, 1, 6, 5, 4, 3, 2, 6, 4, 3]
        quicksort_recursion_inplace_2(array)
        target_array.sort()
        self.assertEqual(target_array, target_array)

    def test_example_3(self):
        array, expected = [6, 1, 3, 110, 123, 2, 5, 0], [6, 1, 3, 110, 123, 2, 5, 0]
        quicksort_recursion_inplace_2(array)
        expected.sort()
        self.assertEqual(expected, array)

    def test_example_4(self):
        target_array, array = [9, 8, 7, 3, 2, 1, 6, 5, 4, 3, 2, 6, 4, 3], [9, 8, 7, 3, 2, 1, 6, 5, 4, 3, 2, 6, 4, 3]
        quicksort_recursion_inplace_2(target_array)
        array.sort()
        self.assertEqual(array, target_array)

    def test_example_5(self):
        target_array, array = [2, 2, 2, 2, 2, 1, 6, 5, 4, 3, 2, 6, -1, 3], [2, 2, 2, 2, 2, 1, 6, 5, 4, 3, 2, 6, -1, 3]
        quicksort_recursion_inplace_2(target_array)
        array.sort()
        self.assertEqual(array, target_array)


class TestQuicksortRecursive(unittest.TestCase):
    def test_example_0(self):
        array = [8, 7, 6, 1, 0, 9, 2]
        result = quicksort_recursion(array)
        array.sort()
        self.assertEqual(array, result)

    def test_example_1(self):
        array = [1, 5, 4, 2, 7, 6, 4, 2, 12312, 54, 7, 31, 1]
        result = quicksort_recursion(array)
        array.sort()
        self.assertEqual(array, result)

    def test_example_2(self):
        array = [9, 8, 7, 3, 2, 1, 6, 5, 4, 3, 2, 6, 4, 3]
        result = quicksort_recursion(array)
        array.sort()
        self.assertEqual(array, result)

    def test_example_3(self):
        array = [6, 1, 3, 110, 123, 2, 5, 0]
        result = quicksort_recursion(array)
        array.sort()
        self.assertEqual(array, result)
