"""
Solution for LC#190: Reverse Bits
https://leetcode.com/problems/reverse-bits/
"""
import unittest


class Solution:
    def reverseBits(self, n: int) -> int:
        reversed_number = 0

        # Iterate over all 32 bits of the given number
        for _ in range(32):
            print(f"Current n: {n:08b}")
            is_last_bit_set = n & 1
            shift_all_bits_to_left = reversed_number << 1
            reversed_number = shift_all_bits_to_left + is_last_bit_set
            print(f"Current reversed_number: {reversed_number:08b}")
            n = n >> 1
            print(f"Current n after adjustments: {n:08b}")

        return reversed_number


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_example_1(self):
        n = int("00000010100101000001111010011100", 2)
        # The input binary string 00000010100101000001111010011100 represents the unsigned integer 43261596,
        # so return 964176192 which its binary representation is 00111001011110000010100101000000.
        self.assertEqual(964176192, self.solution.reverseBits(n))

    def test_example_2(self):
        n = int("11111111111111111111111111111101", 2)
        # The input binary string 11111111111111111111111111111101 represents the unsigned integer 4294967293,
        # so return 3221225471 which its binary representation is 10111111111111111111111111111111.
        self.assertEqual(3221225471, self.solution.reverseBits(n))
