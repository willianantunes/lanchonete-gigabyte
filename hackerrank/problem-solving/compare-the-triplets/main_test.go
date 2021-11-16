package main

import (
	"io/ioutil"
	"os"
	"reflect"
	"strconv"
	"strings"
	"testing"
)

func TestShouldRetrieveResultScenario1(t *testing.T) {
	// Arrange
	inputA := []int32{1, 2, 3}
	inputB := []int32{3, 2, 1}
	expectedResult := []int32{1, 1}
	// Act
	result := compareTriplets(inputA, inputB)
	// Assert
	if !reflect.DeepEqual(result, expectedResult) {
		t.Errorf("compareTriplets() = %v, want %v", result, expectedResult)
	}
}

func TestShouldRetrieveResultScenario2(t *testing.T) {
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
	expectedResult := []int64{1, 1}
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
	// Converting []string to []int
	finalResult := strings.Fields(result[0])
	var finalResultAsSlice []int64
	for _, value := range finalResult {
		valueAsInt, _ := strconv.ParseInt(value, 10, 32)
		finalResultAsSlice = append(finalResultAsSlice, valueAsInt)
	}
	if !reflect.DeepEqual(finalResultAsSlice, expectedResult) {
		t.Errorf("Got %v, want %v", result, expectedResult)
	}
}

func TestShouldRetrieveResultScenario3(t *testing.T) {
	// Arrange
	sampleInputFile, err := os.Open("testdata/sample-2.log")
	if err != nil {
		t.Errorf("Error while opening the file: %s", err)
	}
	oldStdin := os.Stdin
	defer func() { os.Stdin = oldStdin }()
	os.Stdin = sampleInputFile
	outputFileName := "sample-2-output.txt"
	defer func() { os.Remove(outputFileName) }()
	err = os.Setenv("OUTPUT_PATH", outputFileName)
	if err != nil {
		t.Errorf("Error while setting ENV variable: %s", err)
	}
	expectedResult := []int64{2, 1}
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
	// Converting []string to []int
	finalResult := strings.Fields(result[0])
	var finalResultAsSlice []int64
	for _, value := range finalResult {
		valueAsInt, _ := strconv.ParseInt(value, 10, 32)
		finalResultAsSlice = append(finalResultAsSlice, valueAsInt)
	}
	if !reflect.DeepEqual(finalResultAsSlice, expectedResult) {
		t.Errorf("Got %v, want %v", result, expectedResult)
	}
}

func TestShouldPanicGivenNumberEntryFromAIsInvalid(t *testing.T) {
	// Arrange
	inputA := []int32{-1, 2, 3}
	inputB := []int32{3, 2, 1}
	// Act
	expectedMessage := "Constraint! Input A (false) or B (true) is invalid"
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
	compareTriplets(inputA, inputB)
}

func TestShouldPanicGivenNumberEntryFromBIsInvalid(t *testing.T) {
	// Arrange
	inputA := []int32{1, 2, 3}
	inputB := []int32{101, 2, 1}
	// Act
	expectedMessage := "Constraint! Input A (true) or B (false) is invalid"
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
	compareTriplets(inputA, inputB)
}

func readFromFile(filePath string) ([]string, error) {
	fileBytes, err := ioutil.ReadFile(filePath)

	if err != nil {
		return []string{}, err
	}

	return strings.Split(string(fileBytes), "\n"), nil
}
