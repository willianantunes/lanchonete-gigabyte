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
 * Complete the 'countSwaps' function below.
 *
 * The function accepts INTEGER_ARRAY a as parameter.
 */
func countSwaps(array []int32) {
	// Control variables
	var numSwaps int32 = 0
	arrayLength := len(array)
	// Do the thing
	for limiter := arrayLength - 1; limiter > 0; limiter-- {
		for currentPosition := 0; currentPosition < limiter; currentPosition++ {
			rightPositionIndex := currentPosition + 1
			leftValue := array[currentPosition]
			rightValue := array[rightPositionIndex]
			if leftValue > rightValue {
				temporaryHolder := leftValue
				array[currentPosition] = rightValue
				array[rightPositionIndex] = temporaryHolder
				numSwaps++
			}
		}
	}
	// Printing
	firstElement := array[0]
	lastElement := array[arrayLength-1]
	fmt.Printf("Array is sorted in %d swaps.\n", numSwaps)
	fmt.Printf("First Element: %d\n", firstElement)
	fmt.Printf("Last Element: %d\n", lastElement)
}

func main() {
	reader := bufio.NewReaderSize(os.Stdin, 16*1024*1024)

	nTemp, err := strconv.ParseInt(strings.TrimSpace(readLine(reader)), 10, 64)
	checkError(err)
	n := int32(nTemp)

	aTemp := strings.Split(strings.TrimSpace(readLine(reader)), " ")

	var a []int32

	for i := 0; i < int(n); i++ {
		aItemTemp, err := strconv.ParseInt(aTemp[i], 10, 64)
		checkError(err)
		aItem := int32(aItemTemp)
		a = append(a, aItem)
	}

	countSwaps(a)
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
