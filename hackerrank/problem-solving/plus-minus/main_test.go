package main

import (
	"testing"
)

func TestShouldPrintRatioDetailsAboutElementsScenario1(t *testing.T) {
	// Arrange
	input := []int32{1, 1, 0, -1, -1}
	// Act and manually assert
	// expectedResult := []float32{0.400000, 0.400000, 0.200000}
	plusMinus(input)
}

func TestShouldPrintRatioDetailsAboutElementsScenario2(t *testing.T) {
	// Arrange
	input := []int32{-4, 3, -9, 0, 4, 1}
	// Act and manually assert
	// expectedResult := []float32{0.400000, 0.400000, 0.200000}
	plusMinus(input)
}
