package main

import (
	"fmt"
	"time"
)

func SieveOfSundaram(n int) []int {
	nNew := (n - 1) / 2

	// This will be used to mark numbers of the form i+j+2ij
	marked := make([]bool, nNew+1)

	// Mark all numbers of the form i + j + 2ij
	for i := 1; i <= nNew; i++ {
		j := i
		for i+j+2*i*j <= nNew {
			marked[i+j+2*i*j] = true
			j++
		}
	}

	// Prepare list of primes
	primes := []int{2}
	for i := 1; i <= nNew; i++ {
		if !marked[i] {
			primes = append(primes, 2*i+1)
		}
	}

	return primes
}

func main() {
	n := 1000000000

	// Start the timer
	startTime := time.Now()

	primes := SieveOfSundaram(n)

	// End the timer
	elapsed := time.Since(startTime)

	fmt.Printf("Found %d primes up to %d.\n", len(primes), n)
	fmt.Printf("Time taken: %v\n", elapsed)
}
