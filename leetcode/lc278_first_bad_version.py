"""
Solution for LC#278: First Bad Version
https://leetcode.com/problems/first-bad-version/
"""
import unittest


class Solution:
    def __init__(self, bad_version: int):
        self.bad_version = bad_version

    def isBadVersion(self, version: int) -> bool:
        """
        This method is implicitly defined for you on Leetcode.
        I'm just defining it here, so I can test the solution.
        """
        return version >= self.bad_version

    def firstBadVersion(self, n: int) -> int:
        number_of_versions = n
        pointer_left, pointer_right = 0, number_of_versions - 1
        end_with_is_bad_version = False

        while pointer_left <= pointer_right:
            middle_index = pointer_left + (pointer_right - pointer_left) // 2
            supposed_middle_value = middle_index + 1
            if self.isBadVersion(supposed_middle_value):
                pointer_right = middle_index - 1
                end_with_is_bad_version = True
            else:
                pointer_left = middle_index + 1
                end_with_is_bad_version = False

        return supposed_middle_value if end_with_is_bad_version else supposed_middle_value + 1


class TestSolution(unittest.TestCase):
    def test_example_1(self):
        n = 5
        bad = 4
        self.solution = Solution(bad)
        self.assertEqual(bad, self.solution.firstBadVersion(n))

    def test_example_2(self):
        n = 1
        bad = 1
        self.solution = Solution(bad)
        self.assertEqual(bad, self.solution.firstBadVersion(n))

    def test_example_3(self):
        n = 25
        bad = 21
        self.solution = Solution(bad)
        self.assertEqual(bad, self.solution.firstBadVersion(n))

    def test_example_4(self):
        n = 18
        bad = 4
        self.solution = Solution(bad)
        self.assertEqual(bad, self.solution.firstBadVersion(n))

    def test_example_5(self):
        n = 18
        bad = 9
        self.solution = Solution(bad)
        self.assertEqual(bad, self.solution.firstBadVersion(n))

    def test_example_6(self):
        n = 18
        bad = 3
        self.solution = Solution(bad)
        self.assertEqual(bad, self.solution.firstBadVersion(n))

    def test_example_7(self):
        n = 18
        bad = 2
        self.solution = Solution(bad)
        self.assertEqual(bad, self.solution.firstBadVersion(n))

    def test_example_8(self):
        n = 1_926_205_968
        bad = 1_167_880_583
        self.solution = Solution(bad)
        self.assertEqual(bad, self.solution.firstBadVersion(n))
