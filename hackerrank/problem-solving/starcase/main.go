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
 * Complete the 'staircase' function below.
 *
 * The function accepts INTEGER n as parameter.
 */

func staircase(n int32) {
	staircaseSize := int(n)
	// Helper inner function
	retrieveStringFilledWith := func(charToFill string, instances int, spacesInstances int) string {
		var charToFillResult string
		var spacesToFillResult string

		for i := 0; i < instances; i++ {
			charToFillResult += charToFill
		}
		for i := 0; i < spacesInstances; i++ {
			spacesToFillResult += " "
		}

		finalResult := spacesToFillResult + charToFillResult
		return finalResult
	}
	// Doing the logic and print what is requested
	for staircaseCurrentFloor := 1; staircaseCurrentFloor <= staircaseSize; staircaseCurrentFloor++ {
		sharpInstances := staircaseCurrentFloor
		spacesInstances := staircaseSize - staircaseCurrentFloor
		staircaseFloorToBePrinted := retrieveStringFilledWith("#", sharpInstances, spacesInstances)
		fmt.Println(staircaseFloorToBePrinted)
	}
}

func main() {
	reader := bufio.NewReaderSize(os.Stdin, 16*1024*1024)

	nTemp, err := strconv.ParseInt(strings.TrimSpace(readLine(reader)), 10, 64)
	checkError(err)
	n := int32(nTemp)

	staircase(n)
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
