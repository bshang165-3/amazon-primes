def sieve_of_eratosthenes(n):
    """Return a list of all prime numbers up to n."""
    # Create a boolean array "prime[0..n]" and initialize all entries as true.
    # A value in prime[i] will finally be false if i is not a prime, else true bool val.
    prime = [True for _ in range(n+1)]
    p = 2
    while p**2 <= n:
        
        # If prime[p] is not changed, then it is a prime
        if prime[p] is True:
            
            # Update all multiples of p
            for i in range(p**2, n+1, p):
                prime[i] = False
        p += 1
    
    # Collecting the prime numbers
    for p in range(2, n+1):
        if prime[p]:
            primes.append(p)
            
    return primes


primes = []

limit = 100
print(sieve_of_eratosthenes(limit))