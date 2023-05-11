"""
Solution for LC#567: Permutation in String
https://leetcode.com/problems/permutation-in-string/
"""
import unittest


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        database_of_s1 = {}
        database_of_s2 = {}

        for char in s1:
            counter = database_of_s1.get(char, 0) + 1
            database_of_s1[char] = counter
        for char in s2:
            counter = database_of_s2.get(char, 0) + 1
            database_of_s2[char] = counter
        for key in s1:
            counter = database_of_s2.get(key)
            if not counter:
                return False

        queue = []

        for index, char in enumerate(s2):
            if char in database_of_s1:
                counter = database_of_s1.pop(char)
                if counter > 1:
                    counter -= 1
                    database_of_s1[char] = counter
                queue.append((char, counter))
                index_position = index + 2
                value = s2[index + 1 : index_position]
                while database_of_s1.keys():
                    if value not in database_of_s1:
                        break
                    counter = database_of_s1.pop(value)
                    if counter > 1:
                        counter -= 1
                        database_of_s1[value] = counter
                    queue.append((value, counter))
                    previous_index, index_position = index_position, index_position + 1
                    value = s2[previous_index:index_position]
                if not database_of_s1.keys():
                    return True
                while queue:
                    key, counter = queue.pop()
                    has_element = database_of_s1.get(key)
                    if has_element is not None:
                        counter = database_of_s1[key] + 1
                        database_of_s1[key] = counter
                    else:
                        database_of_s1[key] = counter

        return False


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_example_1(self):
        s1 = "ab"
        s2 = "eidbaooo"
        self.assertEqual(True, self.solution.checkInclusion(s1, s2))

    def test_example_2(self):
        s1 = "ab"
        s2 = "eidboaoo"
        self.assertEqual(False, self.solution.checkInclusion(s1, s2))

    def test_example_3(self):
        s1 = "ab"
        s2 = "abcder"
        self.assertEqual(True, self.solution.checkInclusion(s1, s2))

    def test_example_4(self):
        s1 = "abc"
        s2 = "cabgh"
        self.assertEqual(True, self.solution.checkInclusion(s1, s2))

    def test_example_5(self):
        s1 = "abc"
        s2 = "ccccbbbbaaaa"
        self.assertEqual(False, self.solution.checkInclusion(s1, s2))

    def test_example_6(self):
        s1 = "abc"
        s2 = "cccbbbbaaaa"
        self.assertEqual(False, self.solution.checkInclusion(s1, s2))

    def test_example_7(self):
        s1 = "ccc"
        s2 = "cbac"
        self.assertEqual(False, self.solution.checkInclusion(s1, s2))
