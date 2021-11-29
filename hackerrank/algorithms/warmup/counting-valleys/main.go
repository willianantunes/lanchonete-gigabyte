package main

import (
	"bufio"
	"fmt"
	"io"
	"os"
	"strconv"
	"strings"
)

/*
 * Complete the 'countingValleys' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts following parameters:
 *  1. INTEGER steps
 *  2. STRING path
 */
func countingValleys(steps int32, path string) int32 {
	// Control variables
	currentLevel := 0
	var counter int32 = 0
	uphill := 'U'
	downhill := 'D'
	countedBelowSeaLevel := false
	// Dealer
	for _, char := range path {
		// Walking
		if char == uphill {
			currentLevel++
		} else if char == downhill {
			currentLevel--
		} else {
			panic("We received a wrong path!")
		}
		// Evaluating and count if criteria is met
		if currentLevel < 0 && countedBelowSeaLevel == false {
			countedBelowSeaLevel = true
			counter++
		} else if currentLevel >= 0 {
			countedBelowSeaLevel = false
		}
	}
	return counter
}

func main() {
	reader := bufio.NewReaderSize(os.Stdin, 16*1024*1024)

	stdout, err := os.Create(os.Getenv("OUTPUT_PATH"))
	checkError(err)

	defer stdout.Close()

	writer := bufio.NewWriterSize(stdout, 16*1024*1024)

	stepsTemp, err := strconv.ParseInt(strings.TrimSpace(readLine(reader)), 10, 64)
	checkError(err)
	steps := int32(stepsTemp)

	path := readLine(reader)

	result := countingValleys(steps, path)

	fmt.Fprintf(writer, "%d\n", result)

	writer.Flush()
}

func readLine(reader *bufio.Reader) string {
	str, _, err := reader.ReadLine()
	if err == io.EOF {
		return ""
	}

	return strings.TrimRight(string(str), "\r\n")
}

func checkError(err error) {
	if err != nil {
		panic(err)
	}
}
