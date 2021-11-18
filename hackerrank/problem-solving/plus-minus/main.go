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
 * Complete the 'plusMinus' function below.
 *
 * The function accepts INTEGER_ARRAY arr as parameter.
 */
func plusMinus(arr []int32) {
	var counterForPositive float64 = 0
	var counterForNegative float64 = 0
	var counterForZero float64 = 0

	for _, number := range arr {
		isNumberValid := -100 <= number && number <= 100

		if !isNumberValid {
			message := fmt.Sprintf("Constraint: Invalid number entry: %v", number)
			panic(message)
		}

		if number > 0 {
			counterForPositive++
		} else if number < 0 {
			counterForNegative++
		} else {
			counterForZero++
		}
	}

	numberOfElements := float64(len(arr))
	ratioForPositive := counterForPositive / numberOfElements
	ratioForNegative := counterForNegative / numberOfElements
	ratioForZero := counterForZero / numberOfElements

	// Print the ratios of positive, negative and zero values in the array.
	// Each value should be printed on a separate line with 6 digits after the decimal.
	// The function should not return a value.
	fixPrecision := func(number float64, digits int32) float64 {
		// Extracting essential data
		pow := math.Pow(10, float64(digits))
		digit := pow * number

		// Answering how do we round it (CEIL or FLOOR)
		_, fractional := math.Modf(digit)
		takeLeastIntegerValueGreaterThanDigit := fractional > 0.5

		var round float64
		if takeLeastIntegerValueGreaterThanDigit {
			round = math.Ceil(digit)
		} else {
			round = math.Floor(digit)
		}

		// Final result
		return round / pow
	}
	fmt.Printf("%.6f\n", fixPrecision(ratioForPositive, 6))
	fmt.Printf("%.6f\n", fixPrecision(ratioForNegative, 6))
	fmt.Printf("%.6f\n", fixPrecision(ratioForZero, 6))
}

func main() {
	reader := bufio.NewReaderSize(os.Stdin, 16*1024*1024)

	nTemp, err := strconv.ParseInt(strings.TrimSpace(readLine(reader)), 10, 64)
	checkError(err)
	n := int32(nTemp)

	arrTemp := strings.Split(strings.TrimSpace(readLine(reader)), " ")

	var arr []int32

	for i := 0; i < int(n); i++ {
		arrItemTemp, err := strconv.ParseInt(arrTemp[i], 10, 64)
		checkError(err)
		arrItem := int32(arrItemTemp)
		arr = append(arr, arrItem)
	}

	plusMinus(arr)
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
