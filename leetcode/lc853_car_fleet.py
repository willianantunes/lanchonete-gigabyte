"""
Solution for LC#853: Car Fleet
https://leetcode.com/problems/car-fleet/
Array / Stack / Monotonic Stack / Sorting
"""
import unittest


class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        number_of_cars = len(position)
        if number_of_cars == 1:
            return number_of_cars

        positions_with_speed = [(position[index], speed[index]) for index in range(number_of_cars)]
        positions_with_speed.sort(key=lambda v: v[0], reverse=True)

        fleet_count = time_to_arrive = 0

        for position, speed in positions_with_speed:
            current_car_time_to_arrive = (target - position) / speed
            if current_car_time_to_arrive > time_to_arrive:
                time_to_arrive = current_car_time_to_arrive
                fleet_count += 1

        return fleet_count


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_example_1(self):
        target = 12
        position = [10, 8, 0, 5, 3]
        speed = [2, 4, 1, 1, 3]
        self.assertEqual(3, self.solution.carFleet(target, position, speed))

    def test_example_2(self):
        target = 10
        position = [3]
        speed = [3]
        self.assertEqual(1, self.solution.carFleet(target, position, speed))

    def test_example_3(self):
        target = 100
        position = [0, 2, 4]
        speed = [4, 2, 1]
        self.assertEqual(1, self.solution.carFleet(target, position, speed))

    def test_example_4(self):
        target = 10
        position = [0, 1, 2]
        speed = [4, 1, 8]
        self.assertEqual(2, self.solution.carFleet(target, position, speed))

    def test_example_5(self):
        target = 10
        position = [0, 2]
        speed = [4, 1]
        self.assertEqual(1, self.solution.carFleet(target, position, speed))

    def test_example_6(self):
        target = 10
        position = [0, 1, 2, 3, 4, 5]
        speed = [5, 1, 2, 3, 4, 5]
        self.assertEqual(5, self.solution.carFleet(target, position, speed))
