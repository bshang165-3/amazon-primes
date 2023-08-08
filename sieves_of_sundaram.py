import datetime
start_time =  datetime.datetime.now()
def sieve_of_sundaram(n):
    """
    Returns a list of prime numbers up to n using the Sieve of Sundaram.
    """
    # Half the value for easier calculations
    n_new = int((n - 2) / 2)

    # Create a list to mark the numbers to be eliminated
    marked = [False] * (n_new + 1)

    # Mark all numbers of the form i + j + 2ij
    for i in range(1, n_new + 1):
        j = i
        while (i + j + 2 * i * j) <= n_new:
            marked[i + j + 2 * i * j] = True
            j += 1

    # Add 2 to the prime list and then add the remaining numbers
    primes = [2]

    for i in range(1, n_new + 1):
        if not marked[i]:
            primes.append(2 * i + 1)

    return primes

s1 = sieve_of_sundaram(1000000000)
print(s1)
print(f"There are {len(s1)} between 0 and 1b")
finish_time =  datetime.datetime.now()
duration = finish_time - start_time
print(f"Start Time: {start_time}")
print(f"Finish Time: {finish_time}")
print(f"Duration of sieve single is 1B: {duration}")