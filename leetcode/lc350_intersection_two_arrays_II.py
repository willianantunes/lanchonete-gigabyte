"""
Solution for LC#350: Intersection of Two Arrays II
https://leetcode.com/problems/contains-duplicate/
"""
import unittest


class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        number_of_entries_in_nums1 = len(nums1)
        number_of_entries_in_nums2 = len(nums2)
        total_number_of_interactions = number_of_entries_in_nums1 + number_of_entries_in_nums2
        entries_counter_nums1 = {}
        entries_counter_nums2 = {}
        index = 0

        def inner_function(target_index, target_list, target_counter):
            value_from_target_list = target_list[target_index]
            counter_value = target_counter.get(value_from_target_list, 0)
            current_counter_value = counter_value + 1
            target_counter[value_from_target_list] = current_counter_value

        while index < total_number_of_interactions:
            if index < number_of_entries_in_nums1 and index < number_of_entries_in_nums2:
                inner_function(index, nums1, entries_counter_nums1)
                inner_function(index, nums2, entries_counter_nums2)
            elif number_of_entries_in_nums1 > index >= number_of_entries_in_nums2:
                inner_function(index, nums1, entries_counter_nums1)
            elif number_of_entries_in_nums2 > index >= number_of_entries_in_nums1:
                inner_function(index, nums2, entries_counter_nums2)
            index += 1

        intersection = []
        keys_nums2 = entries_counter_nums2.keys()
        for key_from_counter_nums1 in entries_counter_nums1.keys():
            if key_from_counter_nums1 in keys_nums2:
                counter_target_key_nums1 = entries_counter_nums1[key_from_counter_nums1]
                counter_target_key_nums2 = entries_counter_nums2[key_from_counter_nums1]
                if counter_target_key_nums1 > counter_target_key_nums2:
                    intersection += [key_from_counter_nums1 for _ in range(counter_target_key_nums2)]
                else:
                    intersection += [key_from_counter_nums1 for _ in range(counter_target_key_nums1)]

        return intersection


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_example_1(self):
        nums1 = [1, 2, 2, 1]
        nums2 = [2, 2]
        self.assertEqual([2, 2], self.solution.intersect(nums1, nums2))

    def test_example_2(self):
        nums1 = [4, 9, 5]
        nums2 = [9, 4, 9, 8, 4]
        self.assertEqual([4, 9], self.solution.intersect(nums1, nums2))
