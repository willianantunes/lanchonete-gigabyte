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
 * Complete the 'jumpingOnClouds' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts INTEGER_ARRAY c as parameter.
 */
func jumpingOnClouds(clouds []int32) int32 {
	// Control variables
	totalClouds := len(clouds)
	var totalJumps int32 = 0
	var thunderheadValue int32 = 1
	// Dealer
	for number := 0; number < totalClouds; number++ {
		thunderheadsOrCumulus := clouds[number]
		isCurrentThunderhead := thunderheadsOrCumulus == thunderheadValue
		if isCurrentThunderhead {
			continue
		} else {
			twoJumpsIndex := number + 2
			oneJumpIndex := number + 1
			isTwoJumpsAllowed := twoJumpsIndex < totalClouds && clouds[twoJumpsIndex] != thunderheadValue
			isOneJumpAllowed := oneJumpIndex < totalClouds && clouds[oneJumpIndex] != thunderheadValue
			if isOneJumpAllowed && isTwoJumpsAllowed {
				number++
				totalJumps++
			} else if isOneJumpAllowed && !isTwoJumpsAllowed {
				totalJumps++
			} else if !isOneJumpAllowed && isTwoJumpsAllowed {
				totalJumps++
			}
		}
	}
	return totalJumps
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

	cTemp := strings.Split(strings.TrimSpace(readLine(reader)), " ")

	var c []int32

	for i := 0; i < int(n); i++ {
		cItemTemp, err := strconv.ParseInt(cTemp[i], 10, 64)
		checkError(err)
		cItem := int32(cItemTemp)
		c = append(c, cItem)
	}

	result := jumpingOnClouds(c)

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
