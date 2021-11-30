package main

import (
	"testing"
)

func TestShouldReturnFrequencyOfLetterAScenario1(t *testing.T) {
	// Arrange
	inputString := "abcac"
	var nLetters int64 = 10
	var expectedResult int64 = 4
	// Act
	result := repeatedString(inputString, nLetters)
	// Assert
	if result != expectedResult {
		t.Errorf("Got %v, want %v", result, expectedResult)
	}
}

func TestShouldReturnFrequencyOfLetterAScenario2(t *testing.T) {
	// Arrange
	inputString := "aba"
	var nLetters int64 = 10
	var expectedResult int64 = 7
	// Act
	result := repeatedString(inputString, nLetters)
	// Assert
	if result != expectedResult {
		t.Errorf("Got %v, want %v", result, expectedResult)
	}
}

func TestShouldReturnFrequencyOfLetterAScenario3(t *testing.T) {
	// Arrange
	inputString := "a"
	var nLetters int64 = 1000000000000
	var expectedResult int64 = 1000000000000
	// Act
	result := repeatedString(inputString, nLetters)
	// Assert
	if result != expectedResult {
		t.Errorf("Got %v, want %v", result, expectedResult)
	}
}
