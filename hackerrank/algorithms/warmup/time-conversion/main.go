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
 * Complete the 'timeConversion' function below.
 *
 * The function is expected to return a STRING.
 * The function accepts STRING s as parameter.
 */
func timeConversion(twelveClockFormat string) string {
	// Must have data
	values := strings.Split(twelveClockFormat, ":")
	hour, _ := strconv.ParseInt(values[0], 10, 8)
	minute, _ := strconv.ParseInt(values[1], 10, 8)
	secondsWithPeriodInformation := values[2]
	seconds, _ := strconv.ParseInt(secondsWithPeriodInformation[:2], 10, 8)
	periodInformation := secondsWithPeriodInformation[2:]
	// Control variables
	isItAnteMeridiem := periodInformation == "AM"
	isItZeroid := isItAnteMeridiem && hour == 12
	var newHourOutput int8
	if isItAnteMeridiem {
		if isItZeroid {
			newHourOutput = 0
		} else {
			newHourOutput = int8(hour)
		}
	} else {
		mustNotLeaveHourValueIntact := hour != 12
		if mustNotLeaveHourValueIntact {
			newHourOutput = int8(hour + 12)
		} else {
			newHourOutput = 12
		}
	}
	return fmt.Sprintf("%.2d:%.2d:%.2d", newHourOutput, minute, seconds)
}

func main() {
	reader := bufio.NewReaderSize(os.Stdin, 16*1024*1024)

	stdout, err := os.Create(os.Getenv("OUTPUT_PATH"))
	checkError(err)

	defer stdout.Close()

	writer := bufio.NewWriterSize(stdout, 16*1024*1024)

	s := readLine(reader)

	result := timeConversion(s)

	fmt.Fprintf(writer, "%s\n", result)

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
