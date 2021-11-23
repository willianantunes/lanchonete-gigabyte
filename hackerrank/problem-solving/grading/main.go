package main

import (
	"bufio"
	"fmt"
	"io"
	"os"
	"strconv"
	"strings"
)

func buildMultipleOf5() []int32 {
	// Given the challenge rules, I can build with the following idea
	list := make([]int32, 0)
	for i := 40; i <= 100; i += 5 {
		list = append(list, int32(i))
	}
	return list
}

/*
 * Complete the 'gradingStudents' function below.
 *
 * The function is expected to return an INTEGER_ARRAY.
 * The function accepts INTEGER_ARRAY grades as parameter.
 */
func gradingStudents(grades []int32) []int32 {
	// Control variables
	finalGrade := make([]int32, len(grades))
	multiplesOf5 := buildMultipleOf5()
	// Helper inner function
	retrieveNextMultipleOf5 := func(value int32) int32 {
		for _, multipleOf5 := range multiplesOf5 {
			if multipleOf5 >= value {
				return multipleOf5
			}
		}
		panic("Squeeze me gently!")
	}
	// Dealer
	for index, gradeValue := range grades {
		isNotFailingGrade := gradeValue >= 38
		if isNotFailingGrade {
			multipleOf5 := retrieveNextMultipleOf5(gradeValue)
			eligibleToBeRounded := (multipleOf5 - gradeValue) < 3
			if eligibleToBeRounded {
				finalGrade[index] = multipleOf5
				continue
			}
		}
		finalGrade[index] = gradeValue
	}
	return finalGrade
}

func main() {
	reader := bufio.NewReaderSize(os.Stdin, 16*1024*1024)

	stdout, err := os.Create(os.Getenv("OUTPUT_PATH"))
	checkError(err)

	defer stdout.Close()

	writer := bufio.NewWriterSize(stdout, 16*1024*1024)

	gradesCount, err := strconv.ParseInt(strings.TrimSpace(readLine(reader)), 10, 64)
	checkError(err)

	var grades []int32

	for i := 0; i < int(gradesCount); i++ {
		gradesItemTemp, err := strconv.ParseInt(strings.TrimSpace(readLine(reader)), 10, 64)
		checkError(err)
		gradesItem := int32(gradesItemTemp)
		grades = append(grades, gradesItem)
	}

	result := gradingStudents(grades)

	for i, resultItem := range result {
		fmt.Fprintf(writer, "%d", resultItem)

		if i != len(result)-1 {
			fmt.Fprintf(writer, "\n")
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
