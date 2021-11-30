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
 * Complete the 'repeatedString' function below.
 *
 * The function is expected to return a LONG_INTEGER.
 * The function accepts following parameters:
 *  1. STRING s
 *  2. LONG_INTEGER n
 */
func repeatedString(s string, n int64) int64 {
	// Control variables
	var numberOfOccurrences int64 = 0
	letterToBeCounted := 'a'
	receivedLetters := []rune(s)
	countOfLetters := len(receivedLetters)
	var countOfInteractions int64 = 0
	// Dealer
	for index := 0; index < countOfLetters; index++ {
		currentLetter := receivedLetters[index]
		increaseCounter := currentLetter == letterToBeCounted
		if increaseCounter {
			numberOfOccurrences++
		}
		// Getting back to the beginning if required
		isItTheLastIndex := index == (countOfLetters - 1)
		if isItTheLastIndex {
			index = -1
		}
		// In order to stop the infinite loop if criteria is met
		countOfInteractions++
		mustFinishInfiniteLoop := countOfInteractions == n
		if mustFinishInfiniteLoop {
			break
		}
	}
	return numberOfOccurrences
}

func main() {
	reader := bufio.NewReaderSize(os.Stdin, 16*1024*1024)

	stdout, err := os.Create(os.Getenv("OUTPUT_PATH"))
	checkError(err)

	defer stdout.Close()

	writer := bufio.NewWriterSize(stdout, 16*1024*1024)

	s := readLine(reader)

	n, err := strconv.ParseInt(strings.TrimSpace(readLine(reader)), 10, 64)
	checkError(err)

	result := repeatedString(s, n)

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
