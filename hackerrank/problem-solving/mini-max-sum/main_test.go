package main

import (
	"testing"
)

func TestShouldPrintMinimumMaximumScenario1(t *testing.T) {
	// Arrange
	input := []int32{1, 3, 5, 7, 9}
	// Act
	miniMaxSum(input)
}

func TestShouldPrintMinimumMaximumScenario2(t *testing.T) {
	// Arrange
	input := []int32{1, 2, 3, 4, 5}
	// Act
	miniMaxSum(input)
}
