package main

import (
	"io/ioutil"
	"os"
	"strconv"
	"strings"
	"testing"
)

/*
1 2 3
4 5 6
9 8 9

The left-to-right diagonal `1+5+9=15`. The right to left diagonal `3+5+9=17.
Their absolute difference is `15-17=2`.
*/
func TestShouldRetrieveDiagonalDifferenceScenario1(t *testing.T) {
	// Arrange
	input := [][]int32{
		{1, 2, 3},
		{4, 5, 6},
		{9, 8, 9},
	}
	var expectedResult int32 = 2
	// Act
	result := diagonalDifference(input)
	// Assert
	if result != expectedResult {
		t.Errorf("Got %v, want %v", result, expectedResult)
	}
}

func TestShouldRetrieveDiagonalDifferenceScenario2(t *testing.T) {
	// Arrange
	input := [][]int32{
		{11, 2, 4},
		{4, 5, 6},
		{10, 8, -12},
	}
	var expectedResult int32 = 15
	// Act
	result := diagonalDifference(input)
	// Assert
	if result != expectedResult {
		t.Errorf("Got %v, want %v", result, expectedResult)
	}
}

func TestShouldRetrieveDiagonalDifferenceScenario3(t *testing.T) {
	// Arrange
	sampleInputFile, err := os.Open("testdata/sample-1.log")
	if err != nil {
		t.Errorf("Error while opening the file: %s", err)
	}
	oldStdin := os.Stdin
	defer func() { os.Stdin = oldStdin }()
	os.Stdin = sampleInputFile
	outputFileName := "sample-1-output.txt"
	defer func() { os.Remove(outputFileName) }()
	err = os.Setenv("OUTPUT_PATH", outputFileName)
	if err != nil {
		t.Errorf("Error while setting ENV variable: %s", err)
	}
	var expectedResult int64 = 19600
	// Act
	main()
	// Assert
	result, err := readFromFile(outputFileName)
	if err != nil {
		t.Errorf("Output file could not be opened: %s", err)
	}
	if len(result) != 2 && result[1] != "" {
		t.Errorf("Output file seems wrong")
	}
	sum, _ := strconv.ParseInt(result[0], 10, 64)
	if sum != expectedResult {
		t.Errorf("Got %v, want %v", result, expectedResult)
	}
}

func readFromFile(filePath string) ([]string, error) {
	fileBytes, err := ioutil.ReadFile(filePath)

	if err != nil {
		return []string{}, err
	}

	return strings.Split(string(fileBytes), "\n"), nil
}
