package main

import (
	"testing"
)

func TestShouldInformMinimumNumberOfJumpsScenario1(t *testing.T) {
	// Arrange
	input := []int32{0, 1, 0, 0, 0, 1, 0}
	var expectedResult int32 = 3
	// Act
	result := jumpingOnClouds(input)
	// Assert
	if result != expectedResult {
		t.Errorf("Got %v, want %v", result, expectedResult)
	}
}

func TestShouldInformMinimumNumberOfJumpsScenario2(t *testing.T) {
	// Arrange
	input := []int32{0, 0, 1, 0, 0, 1, 0}
	var expectedResult int32 = 4
	// Act
	result := jumpingOnClouds(input)
	// Assert
	if result != expectedResult {
		t.Errorf("Got %v, want %v", result, expectedResult)
	}
}

func TestShouldInformMinimumNumberOfJumpsScenario3(t *testing.T) {
	// Arrange
	input := []int32{0, 0, 0, 0, 1, 0}
	var expectedResult int32 = 3
	// Act
	result := jumpingOnClouds(input)
	// Assert
	if result != expectedResult {
		t.Errorf("Got %v, want %v", result, expectedResult)
	}
}
