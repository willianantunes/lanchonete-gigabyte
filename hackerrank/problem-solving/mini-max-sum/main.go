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
 * Complete the 'miniMaxSum' function below.
 *
 * The function accepts INTEGER_ARRAY arr as parameter.
 */
func miniMaxSum(arr []int32) {
	var minimumValue = int64(math.Pow10(10))
	var maximumValue int64 = -1

	for indexToBeExcluded, _ := range arr {
		var sum int64 = 0
		for index, _ := range arr {
			if indexToBeExcluded == index {
				continue
			}
			value := arr[index]
			sum += int64(value)
		}
		if sum < minimumValue {
			minimumValue = sum
		}
		if sum > maximumValue {
			maximumValue = sum
		}
	}
	fmt.Printf("%v %v", minimumValue, maximumValue)
}

func main() {
	reader := bufio.NewReaderSize(os.Stdin, 16*1024*1024)

	arrTemp := strings.Split(strings.TrimSpace(readLine(reader)), " ")

	var arr []int32

	for i := 0; i < 5; i++ {
		arrItemTemp, err := strconv.ParseInt(arrTemp[i], 10, 64)
		checkError(err)
		arrItem := int32(arrItemTemp)
		arr = append(arr, arrItem)
	}

	miniMaxSum(arr)
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
