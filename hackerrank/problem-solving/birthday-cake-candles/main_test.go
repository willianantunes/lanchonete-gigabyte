package main

import (
	"testing"
)

func TestShouldCountHowManyCandlesAreTallestScenario1(t *testing.T) {
	// Arrange
	input := []int32{4, 4, 1, 3}
	var expectedResult int32 = 2
	// Act
	result := birthdayCakeCandles(input)
	// Assert
	if result != expectedResult {
		t.Errorf("Got = %v, want %v", result, expectedResult)
	}
}

func TestShouldCountHowManyCandlesAreTallestScenario2(t *testing.T) {
	// Arrange
	input := []int32{3, 2, 1, 3}
	var expectedResult int32 = 2
	// Act
	result := birthdayCakeCandles(input)
	// Assert
	if result != expectedResult {
		t.Errorf("Got = %v, want %v", result, expectedResult)
	}
}
