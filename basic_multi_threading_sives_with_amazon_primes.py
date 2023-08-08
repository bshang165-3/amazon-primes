# Multi-threading Sieve of Eratosthenes
import threading
import datetime
import pickle
import concurrent.futures
import sys
# current_limit = sys.getrecursionlimit()
sys.setrecursionlimit(1000000000)
import time

global_primes = [2]

def add_to_primes(item):
    global global_primes 
    global_primes.append(item)

def print_primes():
    global global_primes 
    print("Global Primes:", global_primes)

def if_sieve(i):
    k = i
    if sieve[i] and is_prime(k):
        add_to_primes(i)
        print('found prime', i)
        print(f"Marking all multiples of {i} as non-primes")
        sieve[i*i: n+1: i] = [False] * len(range(i*i, n+1, i))
        time.sleep(0.1)

def is_prime(i):
    for j in global_primes:
        if i % j == 0:
            return False
    return True


def thread_sieve(thread_list, max_threads=100):
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_threads) as executor:
        futures = [executor.submit(if_sieve, i) for i in thread_list]
        concurrent.futures.wait(futures)

if __name__ == "__main__":
    start_time =  datetime.datetime.now()
    n = 1000000000 # One billion; Adjust as Accordingly
    print("n is one billion; adjust as accordingly", n)
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False 
    i = 2
    sieve[i*i: n+1: i] = [False] * len(range(i*i, n+1, i))
    n_list = range(3, int(n**0.5) + 1)
    thread_sieve(n_list)

    print([x for x in range(n + 1) if sieve[x]])
    print(f"There are {len([x for x in range(n + 1) if sieve[x]])} primes in one billion")
    finish_time =  datetime.datetime.now()
    duration = finish_time - start_time
    print(f"Start Time: {start_time}")
    print(f"Finish Time: {finish_time}")
    print(f"Duration: {duration}")
