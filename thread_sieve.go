package main

import (
	"fmt"
	"runtime"
	"sync"
	"time"
)

func SieveOfEratosthenes(n int) []int {
	isPrime := make([]bool, n+1)
	for i := 2; i <= n; i++ {
		isPrime[i] = true
	}

	var wg sync.WaitGroup
	for p := 2; p*p <= n; p++ {
		if isPrime[p] {
			wg.Add(1)
			go func(p int) {
				defer wg.Done()
				for i := p * p; i <= n; i += p {
					isPrime[i] = false
				}
			}(p)
		}
		wg.Wait()
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
	runtime.GOMAXPROCS(runtime.NumCPU()) // Use all available CPU cores
	//runtime.GOMAXPROCS(1) // Use only one CPU core
	n := 100000 // Change this value to find primes up to another number

	startTime := time.Now()

	primes := SieveOfEratosthenes(n)

	endTime := time.Now()

	duration := endTime.Sub(startTime)

	fmt.Println("Number of primes:", len(primes))
	fmt.Printf("Time taken: %v\n", duration)
}
