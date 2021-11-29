package main

import (
	"strings"
	"testing"
)

func TestCountNumberOfValleysTraversedScenario1(t *testing.T) {
	// Arrange
	path := "UDDDUDUU"
	steps := int32(len(strings.Split(path, "")))
	var expectedResult int32 = 1
	// Act
	result := countingValleys(steps, path)
	// Assert
	if result != expectedResult {
		t.Errorf("Got %v, want %v", result, expectedResult)
	}
}

func TestCountNumberOfValleysTraversedScenario2(t *testing.T) {
	// Arrange
	path := "DDUUUUDD"
	steps := int32(len(strings.Split(path, "")))
	var expectedResult int32 = 1
	// Act
	result := countingValleys(steps, path)
	// Assert
	if result != expectedResult {
		t.Errorf("Got %v, want %v", result, expectedResult)
	}
}
