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
 * Complete the 'diagonalDifference' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts 2D_INTEGER_ARRAY arr as parameter.
 */
func diagonalDifference(arr [][]int32) int32 {
	var totalLeftToRightDiagonalValue int32 = 0
	var totalRightToLeftDiagonalValue int32 = 0

	for index, row := range arr {
		// Extracting values
		leftToRightDiagonalValue := row[index]
		rightToLeftDiagonalIndex := (len(row) - 1) - index
		rightToLeftDiagonalValue := row[rightToLeftDiagonalIndex]
		// Are the values valid? 🤔
		isLeftToRightDiagonalValueValid := -100 <= leftToRightDiagonalValue && leftToRightDiagonalValue <= 100
		isRightToLeftDiagonalValue := -100 <= rightToLeftDiagonalValue && rightToLeftDiagonalValue <= 100
		if !isLeftToRightDiagonalValueValid || !isRightToLeftDiagonalValue {
			message := fmt.Sprintf("Constraint: Invalid numbers for left to right (%t) or right to left (%t)", isLeftToRightDiagonalValueValid, isRightToLeftDiagonalValue)
			panic(message)
		}
		totalLeftToRightDiagonalValue += leftToRightDiagonalValue
		totalRightToLeftDiagonalValue += rightToLeftDiagonalValue
	}
	result := totalLeftToRightDiagonalValue - totalRightToLeftDiagonalValue
	return int32(math.Abs(float64(result)))
}

func main() {
	reader := bufio.NewReaderSize(os.Stdin, 16*1024*1024)

	stdout, err := os.Create(os.Getenv("OUTPUT_PATH"))
	checkError(err)

	defer stdout.Close()

	writer := bufio.NewWriterSize(stdout, 16*1024*1024)

	nTemp, err := strconv.ParseInt(strings.TrimSpace(readLine(reader)), 10, 64)
	checkError(err)
	n := int32(nTemp)

	var arr [][]int32
	for i := 0; i < int(n); i++ {
		arrRowTemp := strings.Split(strings.TrimRight(readLine(reader), " \t\r\n"), " ")

		var arrRow []int32
		for _, arrRowItem := range arrRowTemp {
			arrItemTemp, err := strconv.ParseInt(arrRowItem, 10, 64)
			checkError(err)
			arrItem := int32(arrItemTemp)
			arrRow = append(arrRow, arrItem)
		}

		if len(arrRow) != int(n) {
			panic("Bad input")
		}

		arr = append(arr, arrRow)
	}

	result := diagonalDifference(arr)

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
