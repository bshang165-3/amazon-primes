package main

import (
	"fmt"
	"time"
)

func SieveOfEratosthenes(n int) []int {
	isPrime := make([]bool, n+1)
	for i := 2; i <= n; i++ {
		isPrime[i] = true
	}

	for p := 2; p*p <= n; p++ {
		if isPrime[p] {
			for i := p * p; i <= n; i += p {
				isPrime[i] = false
			}
		}
	}

	var primes []int
	for i := 2; i <= n; i++ {
		if isPrime[i] {
			primes = append(primes, i)
		}
	}
	return primes
}

func main() {
	n := 10000000000 // Change this value to find primes up to another number

	startTime := time.Now()

	primes := SieveOfEratosthenes(n)

	endTime := time.Now()

	duration := endTime.Sub(startTime)

	//fmt.Println(primes)
	fmt.Printf("Number of primes up to %d: %d\n", n, len(primes))
	fmt.Printf("Time taken: %v\n", duration)
}
