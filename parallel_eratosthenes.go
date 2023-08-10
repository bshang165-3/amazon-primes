package main

import (
	"fmt"
	"sync"
	"time"
)

func main() {
	n := 1000000000 // Adjust as needed

	startTime := time.Now()

	primes := SieveOfEratosthenesParallel(n)

	duration := time.Since(startTime)

	fmt.Printf("Found %d primes in %v\n", len(primes), duration)
}

func SieveOfEratosthenesParallel(n int) []int {
	var primes []int
	isComposite := make([]bool, n+1)
	var wg sync.WaitGroup

	// Create a channel to pass numbers to goroutines
	ch := make(chan int)

	go func() {
		for i := 2; i <= n; i++ {
			if !isComposite[i] {
				ch <- i
			}
		}
		close(ch)
	}()

	// Spawn multiple Goroutines to process the numbers concurrently
	for i := 0; i < 4; i++ { // Use 4 as an example, can be adjusted based on your CPU
		wg.Add(1)
		go func() {
			for prime := range ch {
				primes = append(primes, prime)
				for j := prime * prime; j <= n; j += prime {
					isComposite[j] = true
				}
			}
			wg.Done()
		}()
	}

	wg.Wait()
	return primes
}
