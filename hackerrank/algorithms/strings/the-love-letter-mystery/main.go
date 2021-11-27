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
 * Complete the 'theLoveLetterMystery' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts STRING s as parameter.
 */
func theLoveLetterMystery(input string) int32 {
	// Control variables
	limitValue := 'a'
	var counterOfOperations int32 = 0
	inputAsRune := []rune(input)
	length := len(inputAsRune)
	// Helper inner function
	decreaseIfPossibleAndInformIt := func(runes *[]rune, index int) bool {
		runesValue := *runes
		value := runesValue[index]
		if value > limitValue {
			runesValue[index]--
			return true
		} else {
			return false
		}
	}
	// Sanity checks
	isItZeroOperations := length == 1
	if isItZeroOperations {
		return counterOfOperations
	}
	// Do the thing
	for leftSideIndex := 0; leftSideIndex < length; leftSideIndex++ {
		rightSideIndex := (length - 1) - leftSideIndex
		invalidToBeEvaluated := rightSideIndex == leftSideIndex
		if invalidToBeEvaluated {
			continue
		}
		// Collecting values
		leftSideValue := inputAsRune[leftSideIndex]
		rightSideValue := inputAsRune[rightSideIndex]
		// Evaluations
		areBothEqual := leftSideValue == rightSideValue
		if !areBothEqual {
			isLeftGreater := leftSideValue > rightSideValue
			var hasDecreased = false
			if isLeftGreater {
				hasDecreased = decreaseIfPossibleAndInformIt(&inputAsRune, leftSideIndex)
			} else {
				hasDecreased = decreaseIfPossibleAndInformIt(&inputAsRune, rightSideIndex)
			}
			if hasDecreased {
				counterOfOperations++
				leftSideIndex--
			}
		}
	}
	return counterOfOperations
}

func main() {
	reader := bufio.NewReaderSize(os.Stdin, 16*1024*1024)

	stdout, err := os.Create(os.Getenv("OUTPUT_PATH"))
	checkError(err)

	defer stdout.Close()

	writer := bufio.NewWriterSize(stdout, 16*1024*1024)

	qTemp, err := strconv.ParseInt(strings.TrimSpace(readLine(reader)), 10, 64)
	checkError(err)
	q := int32(qTemp)

	for qItr := 0; qItr < int(q); qItr++ {
		s := readLine(reader)

		result := theLoveLetterMystery(s)

		fmt.Fprintf(writer, "%d\n", result)
	}

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
