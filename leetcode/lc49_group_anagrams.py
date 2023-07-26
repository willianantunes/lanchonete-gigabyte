"""
Solution for LC#49: Group Anagrams
https://leetcode.com/problems/group-anagrams/
"""
import unittest


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        database = {}
        for chars in strs:
            chars_as_list = list(chars)
            chars_as_list.sort()
            chars_ordered = "".join(chars_as_list)
            group = database.get(chars_ordered, [])
            group.append(chars)
            database[chars_ordered] = group
        groups = []
        for key in database:
            group = database[key]
            groups.append(group)
        return groups


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_example_1(self):
        strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
        self.assertEqual([["eat", "tea", "ate"], ["tan", "nat"], ["bat"]], self.solution.groupAnagrams(strs))
