import datetime
def sieve_of_eratosthenes(n):
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False 
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            print(f"Marking all multiples of {i} as non-primes")
            sieve[i*i: n+1: i] = [False] * len(range(i*i, n+1, i))
    return [x for x in range(n + 1) if sieve[x]]
start_time =  datetime.datetime.now()
primes_to_ten_billion = sieve_of_eratosthenes(10000000000)

print(primes_to_ten_billion)

print(f"There are {len(primes_to_ten_billion)} primes from 0 to 10 billion")
finish_time =  datetime.datetime.now()
duration = finish_time - start_time
print(f"Start Time: {start_time}")
print(f"Finish Time: {finish_time}")
print(f"Duration of sieve single is 10B: {duration}")