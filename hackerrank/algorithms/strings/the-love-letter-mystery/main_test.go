package main

import (
	"reflect"
	"testing"
)

func TestShouldCountNumberOfOperationsScenario1(t *testing.T) {
	// Arrange
	inputs := []string{"abc", "abcba", "abcd", "cba", "cde"}
	results := make([]int32, len(inputs))
	expectedResult := []int32{2, 0, 4, 2, 2}
	// Act
	for index, input := range inputs {
		result := theLoveLetterMystery(input)
		results[index] = result
	}
	// Assert
	if !reflect.DeepEqual(results, expectedResult) {
		t.Errorf("Got %v, want %v", results, expectedResult)
	}
}
