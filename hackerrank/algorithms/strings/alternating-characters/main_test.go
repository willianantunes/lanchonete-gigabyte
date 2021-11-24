package main

import (
	"reflect"
	"testing"
)

func TestAlternateStringScenario1(t *testing.T) {
	// Arrange
	inputs := []string{"AAAA", "BBBBB", "ABABABAB", "BABABA", "AAABBB"}
	results := make([]int32, 5)
	expectedResult := []int32{3, 4, 0, 0, 4}
	// Act
	for index, input := range inputs {
		result := alternatingCharacters(input)
		results[index] = result
	}
	// Assert
	if !reflect.DeepEqual(results, expectedResult) {
		t.Errorf("Got %v, want %v", results, expectedResult)
	}
}
