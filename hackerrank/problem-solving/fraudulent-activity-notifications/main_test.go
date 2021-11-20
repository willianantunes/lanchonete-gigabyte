package main

import (
	"io/ioutil"
	"os"
	"strconv"
	"strings"
	"testing"
)

func TestShouldReceiveActivityNotificationScenario1(t *testing.T) {
	// Arrange
	expenditure := []int32{10, 20, 30, 40, 50}
	var numberOfTrailingDays int32 = 3
	var expectedResult int32 = 1
	// Act
	result := activityNotifications(expenditure, numberOfTrailingDays)
	// Assert
	if result != expectedResult {
		t.Errorf("Got %v, want %v", result, expectedResult)
	}
}

func TestShouldReceiveActivityNotificationScenario2(t *testing.T) {
	// Arrange
	expenditure := []int32{2, 3, 4, 2, 3, 6, 8, 4, 5}
	var numberOfTrailingDays int32 = 5
	var expectedResult int32 = 2
	// Act
	result := activityNotifications(expenditure, numberOfTrailingDays)
	// Assert
	if result != expectedResult {
		t.Errorf("Got %v, want %v", result, expectedResult)
	}
}

func TestShouldReceiveActivityNotificationScenario3(t *testing.T) {
	// Arrange
	expenditure := []int32{1, 2, 3, 4, 4}
	var numberOfTrailingDays int32 = 4
	var expectedResult int32 = 0
	// Act
	result := activityNotifications(expenditure, numberOfTrailingDays)
	// Assert
	if result != expectedResult {
		t.Errorf("Got %v, want %v", result, expectedResult)
	}
}

func TestShouldReceiveActivityNotificationScenario4(t *testing.T) {
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
	var expectedResult int64 = 1026
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
