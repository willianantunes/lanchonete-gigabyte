package main

import (
	"io/ioutil"
	"os"
	"strconv"
	"strings"
	"testing"
)

func TestShouldSumArrayScenario1(t *testing.T) {
	// Arrange
	input := []int32{1, 2, 3}
	var expectedResult int32 = 6
	// Act
	result := simpleArraySum(input)
	if result != expectedResult {
		t.Errorf("simpleArraySum() = %v, want %v", result, expectedResult)
	}
}

func TestShouldSumArrayScenario2(t *testing.T) {
	// Arrange
	sampleInputFile, err := os.Open("testdata/sample-1.log")
	if err != nil {
		t.Errorf("Error while opening the file: %s", err)
	}
	oldStdin := os.Stdin
	defer func() { os.Stdin = oldStdin }()
	os.Stdin = sampleInputFile
	outputFileName := "sample-1-output.txt"
	err = os.Setenv("OUTPUT_PATH", outputFileName)
	if err != nil {
		t.Errorf("Error while setting ENV variable: %s", err)
	}
	var expectedResult int64 = 31
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
	defer func() { os.Remove(outputFileName) }()
}

func TestShouldPanicGivenNumberEntryIsGreaterThan1000(t *testing.T) {
	// Arrange
	input := []int32{1, 2, 1001}
	expectedMessage := "Constraint: Invalid number entry: 1001"
	defer func() {
		// Assert
		r := recover()
		if r != nil {
			message := r.(string)
			if message != expectedMessage {
				t.Errorf("Got `%s`, want `%s`", message, expectedMessage)
			}
		} else {
			t.Error("It should have panicked!")
		}
	}()
	// Act
	simpleArraySum(input)
}

func TestShouldNotPanicGivenNumberEntryIsLessThanEqual1000(t *testing.T) {
	// Arrange
	input := []int32{1, 2, 1000}
	defer func() {
		r := recover()
		if r != nil {
			t.Errorf("It should not have panicked!")
		}
	}()
	// Act
	simpleArraySum(input)
}

func readFromFile(filePath string) ([]string, error) {
	fileBytes, err := ioutil.ReadFile(filePath)

	if err != nil {
		return []string{}, err
	}

	return strings.Split(string(fileBytes), "\n"), nil
}
