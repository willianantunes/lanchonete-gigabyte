package main

import (
	"bufio"
	"fmt"
	"io"
	"math"
	"os"
	"strconv"
	"strings"
)

/*
 * Complete the 'hourglassSum' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts 2D_INTEGER_ARRAY arr as parameter.
 */
func hourglassSum(arr [][]int32) int32 {
	// Control variables
	matrixLength := len(arr)
	limitForRowAndColumn := matrixLength - 1
	startRow, startColumn := 1, 1
	highestValue := math.MinInt32
	// Doing the thing
	for row := startRow; row < limitForRowAndColumn; row++ {
		for column := startColumn; column < limitForRowAndColumn; column++ {
			hourglassMiddleIndex := column
			// Retrieving values
			hourglassUpperLeftValue := arr[row-1][hourglassMiddleIndex-1]
			hourglassUpperMiddleValue := arr[row-1][hourglassMiddleIndex]
			hourglassUpperRightValue := arr[row-1][hourglassMiddleIndex+1]
			hourglassMiddleValue := arr[row][hourglassMiddleIndex]
			hourglassBottomLeftValue := arr[row+1][hourglassMiddleIndex-1]
			hourglassBottomMiddleValue := arr[row+1][hourglassMiddleIndex]
			hourglassBottomRightValue := arr[row+1][hourglassMiddleIndex+1]
			// Sums
			upperSum := hourglassUpperLeftValue + hourglassUpperMiddleValue + hourglassUpperRightValue
			bottomSum := hourglassBottomLeftValue + hourglassBottomMiddleValue + hourglassBottomRightValue
			hourGlassSum := int(upperSum + hourglassMiddleValue + bottomSum)
			// Is it higher than the previous value?
			if hourGlassSum > highestValue {
				highestValue = hourGlassSum
			}
		}
	}
	return int32(highestValue)
}

func main() {
	reader := bufio.NewReaderSize(os.Stdin, 16*1024*1024)

	stdout, err := os.Create(os.Getenv("OUTPUT_PATH"))
	checkError(err)

	defer stdout.Close()

	writer := bufio.NewWriterSize(stdout, 16*1024*1024)

	var arr [][]int32
	for i := 0; i < 6; i++ {
		arrRowTemp := strings.Split(strings.TrimRight(readLine(reader), " \t\r\n"), " ")

		var arrRow []int32
		for _, arrRowItem := range arrRowTemp {
			arrItemTemp, err := strconv.ParseInt(arrRowItem, 10, 64)
			checkError(err)
			arrItem := int32(arrItemTemp)
			arrRow = append(arrRow, arrItem)
		}

		if len(arrRow) != 6 {
			panic("Bad input")
		}

		arr = append(arr, arrRow)
	}

	result := hourglassSum(arr)

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
