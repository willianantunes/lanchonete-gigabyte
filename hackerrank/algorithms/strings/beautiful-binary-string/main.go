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
 * Complete the 'beautifulBinaryString' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts STRING b as parameter.
 */
func beautifulBinaryString(binaryString string) int32 {
	const uglyBinary = "010"
	uglyBinaryLength := len(uglyBinary)
	// Control variables
	var counter int32 = 0
	// Helper inner function
	isUglyBinaryAvailable := func(stringToBeEvaluated string) (bool, int) {
		result := strings.Index(stringToBeEvaluated, uglyBinary)
		return result != -1, result
	}
	// Dealer
	hasUglyString, indexStartAt := isUglyBinaryAvailable(binaryString)
	for hasUglyString {
		counter++
		whereToStart := indexStartAt + uglyBinaryLength
		binaryString = binaryString[whereToStart:]
		indexStartAt = strings.Index(binaryString, uglyBinary)
		hasUglyString = indexStartAt != -1
	}
	return counter
}

func main() {
	reader := bufio.NewReaderSize(os.Stdin, 16*1024*1024)

	stdout, err := os.Create(os.Getenv("OUTPUT_PATH"))
	checkError(err)

	defer stdout.Close()

	writer := bufio.NewWriterSize(stdout, 16*1024*1024)

	nTemp, err := strconv.ParseInt(strings.TrimSpace(readLine(reader)), 10, 64)
	checkError(err)
	_ = int32(nTemp)

	b := readLine(reader)

	result := beautifulBinaryString(b)

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
