package main

import (
	"reflect"
	"testing"
)

func TestShouldRoundGradeScenario1(t *testing.T) {
	// Arrange
	grade := []int32{84, 29, 57}
	expectedFinalGrade := []int32{85, 29, 57}
	// Act
	result := gradingStudents(grade)
	// Assert
	if !reflect.DeepEqual(result, expectedFinalGrade) {
		t.Errorf("Got = %v, want %v", result, expectedFinalGrade)
	}
}

func TestShouldRoundGradeScenario2(t *testing.T) {
	// Arrange
	grade := []int32{73, 67, 38, 33}
	expectedFinalGrade := []int32{75, 67, 40, 33}
	// Act
	result := gradingStudents(grade)
	// Assert
	if !reflect.DeepEqual(result, expectedFinalGrade) {
		t.Errorf("Got = %v, want %v", result, expectedFinalGrade)
	}
}
