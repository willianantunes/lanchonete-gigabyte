package main

import (
	"testing"
)

func TestShouldConvertTimeScenario1(t *testing.T) {
	// Arrange
	input := "12:01:00PM"
	expectedOutput := "12:01:00"
	// Act
	output := timeConversion(input)
	// Assert
	if output != expectedOutput {
		t.Errorf("Got %v, want %v", output, expectedOutput)
	}
}

func TestShouldConvertTimeScenario2(t *testing.T) {
	// Arrange
	input := "12:01:00AM"
	expectedOutput := "00:01:00"
	// Act
	output := timeConversion(input)
	// Assert
	if output != expectedOutput {
		t.Errorf("Got %v, want %v", output, expectedOutput)
	}
}

func TestShouldConvertTimeScenario3(t *testing.T) {
	// Arrange
	input := "07:05:45PM"
	expectedOutput := "19:05:45"
	// Act
	output := timeConversion(input)
	// Assert
	if output != expectedOutput {
		t.Errorf("Got %v, want %v", output, expectedOutput)
	}
}

func TestShouldConvertTimeScenario4(t *testing.T) {
	// Arrange
	input := "06:40:03AM"
	expectedOutput := "06:40:03"
	// Act
	output := timeConversion(input)
	// Assert
	if output != expectedOutput {
		t.Errorf("Got %v, want %v", output, expectedOutput)
	}
}
