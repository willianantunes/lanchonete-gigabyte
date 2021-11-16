package main

import (
	"io/ioutil"
	"os"
	"strconv"
	"strings"
	"testing"
)

func TestShouldRetrieveResultScenario1(t *testing.T) {
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
	var expectedResult int64 = 5000000015
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
