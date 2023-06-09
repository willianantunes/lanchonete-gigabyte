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
        def _first_bad_version(initial_version, last_version: int):
            middle_version = (last_version + initial_version) // 2
            if not self.isBadVersion(middle_version - 1) and self.isBadVersion(middle_version):
                return middle_version

            if not self.isBadVersion(middle_version):
                return _first_bad_version(middle_version + 1, last_version)

            return _first_bad_version(initial_version, middle_version - 1)

        return _first_bad_version(0, n)


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
