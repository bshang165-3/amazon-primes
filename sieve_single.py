import datetime
def sieve_of_eratosthenes(limit):
    primes = [True] * (limit + 1)
    primes[0] = primes[1] = False
    
    for num in range(2, int(limit ** 0.5) + 1):
        if primes[num]:
            print(f"marking multiples of prime number {num} as not prime")
            for multiple in range(num * num, limit + 1, num):
                primes[multiple] = False
    
    return [num for num, is_prime in enumerate(primes) if is_prime]

# Example usage
limit = 100000000
start_time =  datetime.datetime.now()
prime_numbers = sieve_of_eratosthenes(limit)
print("Number of prime numbers up to", limit, "is :", prime_numbers)
finish_time =  datetime.datetime.now()
duration = finish_time - start_time
print(f"Start Time: {start_time}")
print(f"Finish Time: {finish_time}")
print(f"Duration of sieve single is 100M: {duration}")