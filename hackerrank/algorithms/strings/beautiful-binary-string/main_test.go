package main

import (
	"testing"
)

func TestShouldCountNumberOfStepsScenario1(t *testing.T) {
	// Arrange
	input := "0101010"
	var expectedResult int32 = 2
	// Act
	result := beautifulBinaryString(input)
	// Assert
	if result != expectedResult {
		t.Errorf("Got %v, want %v", result, expectedResult)
	}
}

func TestShouldCountNumberOfStepsScenario2(t *testing.T) {
	// Arrange
	input := "01100"
	var expectedResult int32 = 0
	// Act
	result := beautifulBinaryString(input)
	// Assert
	if result != expectedResult {
		t.Errorf("Got %v, want %v", result, expectedResult)
	}
}

func TestShouldCountNumberOfStepsScenario3(t *testing.T) {
	// Arrange
	input := "0100101010"
	var expectedResult int32 = 3
	// Act
	result := beautifulBinaryString(input)
	// Assert
	if result != expectedResult {
		t.Errorf("Got %v, want %v", result, expectedResult)
	}
}
