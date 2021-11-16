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
 * Complete the 'compareTriplets' function below.
 *
 * The function is expected to return an INTEGER_ARRAY.
 * The function accepts following parameters:
 *  1. INTEGER_ARRAY a
 *  2. INTEGER_ARRAY b
 */
func compareTriplets(a []int32, b []int32) []int32 {
	var totalPointsA int32 = 0
	var totalPointsB int32 = 0

	for index, numberForA := range a {
		numberForB := b[index]
		numberForAIsValid := 1 <= numberForA && numberForA <= 100
		numberForBIsValid := 1 <= numberForB && numberForB <= 100

		if !numberForAIsValid || !numberForBIsValid {
			message := fmt.Sprintf("Constraint! Input A (%t) or B (%t) is invalid", numberForAIsValid, numberForBIsValid)
			panic(message)
		}

		pointMustBeReceivedByA := numberForA > numberForB
		pointMustBeReceivedByB := numberForA < numberForB

		if pointMustBeReceivedByA {
			totalPointsA++
		} else if pointMustBeReceivedByB {
			totalPointsB++
		}
	}

	return []int32{totalPointsA, totalPointsB}
}

func main() {
	reader := bufio.NewReaderSize(os.Stdin, 16*1024*1024)

	stdout, err := os.Create(os.Getenv("OUTPUT_PATH"))
	checkError(err)

	defer stdout.Close()

	writer := bufio.NewWriterSize(stdout, 16*1024*1024)

	aTemp := strings.Split(strings.TrimSpace(readLine(reader)), " ")

	var a []int32

	for i := 0; i < 3; i++ {
		aItemTemp, err := strconv.ParseInt(aTemp[i], 10, 64)
		checkError(err)
		aItem := int32(aItemTemp)
		a = append(a, aItem)
	}

	bTemp := strings.Split(strings.TrimSpace(readLine(reader)), " ")

	var b []int32

	for i := 0; i < 3; i++ {
		bItemTemp, err := strconv.ParseInt(bTemp[i], 10, 64)
		checkError(err)
		bItem := int32(bItemTemp)
		b = append(b, bItem)
	}

	result := compareTriplets(a, b)

	for i, resultItem := range result {
		fmt.Fprintf(writer, "%d", resultItem)

		if i != len(result)-1 {
			fmt.Fprintf(writer, " ")
		}
	}

	fmt.Fprintf(writer, "\n")

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
