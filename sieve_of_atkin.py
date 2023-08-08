import datetime
start_time =  datetime.datetime.now()
def sieve_of_atkin(limit):
    P = [2, 3]
    sieve = [0] * (limit + 1)
    for x in range(1, int(limit ** 0.5) + 1):
        for y in range(1, int(limit ** 0.5) + 1):
            n = 4 * x**2 + y**2
            if n <= limit and (n % 12 == 1 or n % 12 == 5):
                sieve[n] = not sieve[n]
            n = 3 * x**2 + y**2
            if n <= limit and n % 12 == 7:
                sieve[n] = not sieve[n]
            n = 3 * x**2 - y**2
            if x > y and n <= limit and n % 12 == 11:
                sieve[n] = not sieve[n]
    for r in range(5, int(limit ** 0.5) + 1):
        if sieve[r]:
            for i in range(r**2, limit + 1, r**2):
                sieve[i] = False
    for a in range(5, limit + 1):
        if sieve[a]:
            P.append(a)
    return P

b1 = sieve_of_atkin(1000000000)
print(b1)
print(f"there are{len(b1)} primes betweeen 0 and 1B")
finish_time =  datetime.datetime.now()
duration = finish_time - start_time
print(f"Start Time: {start_time}")
print(f"Finish Time: {finish_time}")
print(f"Duration of sieve single is 1B: {duration}")