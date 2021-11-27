package main

import (
	"testing"
)

func TestShouldCountSwapsScenario1(t *testing.T) {
	// Arrange
	input := []int32{6, 4, 1}
	// Act and assert manually
	countSwaps(input)
}

func TestShouldCountSwapsScenario2(t *testing.T) {
	// Arrange
	input := []int32{3, 2, 1}
	// Act and assert manually
	countSwaps(input)
}
