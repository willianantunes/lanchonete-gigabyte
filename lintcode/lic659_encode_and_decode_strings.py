"""
Solution for 659: Encode and Decode Strings
https://www.lintcode.com/problem/659/
"""
import unittest


class Solution:
    def encode(self, value: list[str]) -> str:
        encoded_output = []
        for entry in value:
            entry_size = len(entry)
            encoded_output.append(f"{entry_size}#{entry}")
        return "".join(encoded_output)

    def decode(self, value: str) -> list[str]:
        decoded_output = []
        value_length = len(value)
        pointer = 0
        while pointer < value_length:
            expected_dash_index = pointer + 1
            while value[expected_dash_index] != "#":
                expected_dash_index += 1
            dash_position = expected_dash_index + 1
            word_size = int(value[pointer:expected_dash_index])
            word = value[dash_position : dash_position + word_size]
            decoded_output.append(word)
            pointer = dash_position + word_size
        return decoded_output


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_example_1(self):
        values = ["lint", "code", "love", "you"]
        encoded_string = self.solution.encode(values)
        self.assertEqual(values, self.solution.decode(encoded_string))
