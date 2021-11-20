package main

import (
	"bufio"
	"fmt"
	"io"
	"os"
	"strconv"
	"strings"
)

func countingSort(inputPointer *[]int32) *[]int32 {
	input := *inputPointer
	// In order to retrieve the maximum number
	var maximumNumber int32 = -1
	for _, value := range input {
		if value > maximumNumber {
			maximumNumber = value
		}
	}
	// Array to store the count of each number
	var arrayWithCounterOfEachNumber = make([]int32, maximumNumber+1)
	for _, value := range input {
		arrayWithCounterOfEachNumber[value]++
	}
	// Modify de counter array by adding the previous counts
	for index := 1; index < len(arrayWithCounterOfEachNumber); index++ {
		previousElementIndex := index - 1
		previousElementValue := arrayWithCounterOfEachNumber[previousElementIndex]
		arrayWithCounterOfEachNumber[index] += previousElementValue
	}
	// Filling the output array
	var sortedArray = make([]int32, len(input))
	for _, value := range input {
		counterOfValueInstances := arrayWithCounterOfEachNumber[value]
		indexInSortedArray := counterOfValueInstances - 1
		sortedArray[indexInSortedArray] = value
		arrayWithCounterOfEachNumber[value]--
	}
	return &sortedArray
}

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
	receivedNotifications := make(chan int)
	var numberOfNotifications int32 = 0
	totalExpenditures := int32(len(expenditures))
	whereAnalysisStart := numberOfTrailingDays
	// Helper inner functions
	retrieveTrailingExpenditures := func(expenses *[]int32, trailingDays *int32, startPoint *int32) []int32 {
		beginning := *startPoint - *trailingDays
		expensesValue := *expenses
		return expensesValue[beginning:*startPoint]
	}
	retrieveMedian := func(expenses *[]int32) float32 {
		sortedExpensesPointer := countingSort(expenses)
		sortedExpenses := *sortedExpensesPointer
		currentLength := len(sortedExpenses)
		isCurrentLengthOddNumber := currentLength%2 != 0
		if isCurrentLengthOddNumber {
			index := currentLength / 2
			return float32(sortedExpenses[index])
		} else {
			middleRightIndex := currentLength / 2
			middleLeftIndex := middleRightIndex - 1
			middleRight := float32(sortedExpenses[middleRightIndex])
			middleLeft := float32(sortedExpenses[middleLeftIndex])

			return (middleRight + middleLeft) / 2
		}
	}
	dayAnalyser := func(dayToBeAnalysed int32) {
		dayExpenditure := expenditures[dayToBeAnalysed]
		trailingExpenditures := retrieveTrailingExpenditures(&expenditures, &numberOfTrailingDays, &dayToBeAnalysed)
		median := retrieveMedian(&trailingExpenditures)
		shouldSendNotification := float32(dayExpenditure) >= (2 * median)
		if shouldSendNotification {
			receivedNotifications <- 1
		} else {
			receivedNotifications <- 0
		}
	}
	// Dealer
	for dayToBeAnalysed := whereAnalysisStart; dayToBeAnalysed < totalExpenditures; dayToBeAnalysed++ {
		go dayAnalyser(dayToBeAnalysed)
	}
	for dayToBeAnalysed := whereAnalysisStart; dayToBeAnalysed < totalExpenditures; dayToBeAnalysed++ {
		notification := <-receivedNotifications
		numberOfNotifications += int32(notification)
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
