package main

import (
	"testing"
)

func TestShouldCountScenario1(t *testing.T) {
	// Arrange
	input := []int32{10, 20, 20, 10, 10, 30, 50, 10, 20}
	n := int32(len(input))
	var expectedResult int32 = 3
	// Act
	result := sockMerchant(n, input)
	// Assert
	if result != expectedResult {
		t.Errorf("Got %v, want %v", result, expectedResult)
	}
}
