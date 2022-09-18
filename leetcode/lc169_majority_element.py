"""
Solution for LC#169: Majority Element
https://leetcode.com/problems/majority-element/
"""
import unittest


class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        database = {}
        majority = "majority"

        for value in nums:
            counter = database.get(value, 0) + 1
            database[value] = counter
            majority_element = database.get(majority)
            if not majority_element:
                majority_element = (value, counter)
                database[majority] = majority_element
            else:
                m_value, m_counter = majority_element
                if counter > m_counter:
                    majority_element = (value, counter)
                    database[majority] = majority_element

        return database[majority][0]


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_example_1(self):
        nums = [3, 2, 3]
        self.assertEqual(3, self.solution.majorityElement(nums))

    def test_example_2(self):
        nums = [2, 2, 1, 1, 1, 2, 2]
        self.assertEqual(2, self.solution.majorityElement(nums))
