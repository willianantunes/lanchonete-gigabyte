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
 * Complete the 'activityNotifications' function below.
 *
 * Given the number of trailing days `d` and a client's total daily expenditures for a period of `n` days,
 * determine the number of times the client will receive a notification over all `n` days.
 *
 * If the amount spent by a client on a particular day is greater than or equal to 2x the client's
 * median spending for a trailing number of days, they send the client a notification about potential fraud
 * The bank doesn't send the client any notifications until they have at least that trailing number of prior days' transaction data.
 *
 * The function is expected to return an INTEGER.
 * The function accepts following parameters:
 *  1. INTEGER_ARRAY expenditure
 *  2. INTEGER d
 */
func activityNotifications(expenditures []int32, numberOfTrailingDays int32) int32 {
	// Control variables
	var numberOfNotifications int32 = 0
	// See the section constraints to understand why this array has 201 as its length
	const numberConstraintMaximumValue = 201
	var arrayWithCounterOfEachNumber = make([]int32, numberConstraintMaximumValue)
	// Helper inner functions
	sum := func(arr *[]int32) int32 {
		arrValue := *arr
		var result int32 = 0
		for _, v := range arrValue {
			result += v
		}
		return result
	}
	retrieveLastElement := func(arr *[]int32) int32 {
		arrValue := *arr
		return arrValue[len(arrValue)-1]
	}
	retrieveLimitFromTrailingExpenditures := func(counterOfEachNumber []int32, trailingDays int32) int32 {
		var positionIndex int32 = 0
		middleLeftIndex := trailingDays / 2
		middleRightOrIndeedMiddleIndex := middleLeftIndex + 1
		var medianHelper = make([]int32, 0)
		for numberUsedAsIndex, howMuchTheNumberAppears := range counterOfEachNumber {
			positionIndex += howMuchTheNumberAppears
			if len(medianHelper) == 0 && middleLeftIndex <= positionIndex {
				medianHelper = append(medianHelper, int32(numberUsedAsIndex))
			}
			if middleRightOrIndeedMiddleIndex <= positionIndex {
				medianHelper = append(medianHelper, int32(numberUsedAsIndex))
				break
			}
		}
		isTrailingDaysOddNumber := trailingDays%2 != 0
		if isTrailingDaysOddNumber {
			middleElement := retrieveLastElement(&medianHelper)
			return middleElement * 2
		} else {
			// Just sum the two middle elements
			// Since we must multiply by 2 afterwards, we don't need to divide them
			return sum(&medianHelper)
		}
	}
	// Filling the counter up until the day to be analysed
	for _, value := range expenditures[:numberOfTrailingDays] {
		arrayWithCounterOfEachNumber[value]++
	}
	// Dealer
	for index, expenditureValue := range expenditures[numberOfTrailingDays:] {
		limit := retrieveLimitFromTrailingExpenditures(arrayWithCounterOfEachNumber, numberOfTrailingDays)
		shouldSendNotification := expenditureValue >= limit
		if shouldSendNotification {
			numberOfNotifications++
		}
		// Now we increase with the current number
		arrayWithCounterOfEachNumber[expenditureValue]++
		// Then decrease, cleaning the counter and moving the window
		// https://stackoverflow.com/a/64111403/3899136
		// https://youtu.be/MK-NZ4hN7rs
		numberToBeSubtractedFromTheCounter := expenditures[index]
		arrayWithCounterOfEachNumber[numberToBeSubtractedFromTheCounter]--
	}
	return numberOfNotifications
}

func main() {
	reader := bufio.NewReaderSize(os.Stdin, 16*1024*1024)

	stdout, err := os.Create(os.Getenv("OUTPUT_PATH"))
	checkError(err)

	defer stdout.Close()

	writer := bufio.NewWriterSize(stdout, 16*1024*1024)

	firstMultipleInput := strings.Split(strings.TrimSpace(readLine(reader)), " ")

	nTemp, err := strconv.ParseInt(firstMultipleInput[0], 10, 64)
	checkError(err)
	n := int32(nTemp)

	dTemp, err := strconv.ParseInt(firstMultipleInput[1], 10, 64)
	checkError(err)
	d := int32(dTemp)

	expenditureTemp := strings.Split(strings.TrimSpace(readLine(reader)), " ")

	var expenditure []int32

	for i := 0; i < int(n); i++ {
		expenditureItemTemp, err := strconv.ParseInt(expenditureTemp[i], 10, 64)
		checkError(err)
		expenditureItem := int32(expenditureItemTemp)
		expenditure = append(expenditure, expenditureItem)
	}

	result := activityNotifications(expenditure, d)

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
