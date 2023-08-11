# Multi-threading Sieve of Eratosthenes
import threading
import datetime
import pickle
import concurrent.futures
import sys
# current_limit = sys.getrecursionlimit()
sys.setrecursionlimit(5000000)
import time

global_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]

def init_sieve(n):
    global global_sieve
    global_sieve = [True] * (n + 1)
    global_sieve[0] = global_sieve[1] = False
    for i in [2, 3, 5, 7, 11, 13, 17, 19, 23]:
        print("Marking all multiples of", i, "as non-primes")
        global_sieve[i*i: n+1: i] = [False] * len(range(i*i, n+1, i))

def change_sieves(i):
    global global_sieve
    global_sieve[i*i: n+1: i] = [False] * len(range(i*i, n+1, i))

def add_to_primes(item):
    global global_primes 
    global_primes.append(item)

def print_primes():
    global global_primes 
    print("Global Primes:", global_primes)

def if_sieve(i):
    k = i
    if global_sieve[i] and is_prime(k):
        add_to_primes(i)
        print(f"Marking all multiples of {i} as non-primes")
        change_sieves(i)

def is_prime(i):
    for j in global_primes:
        if i % j == 0:
            return False
    return True


def thread_sieve(thread_list, max_threads=10):
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_threads) as executor:
        futures = [executor.submit(if_sieve, i) for i in thread_list]
        concurrent.futures.wait(futures)

if __name__ == "__main__":
    start_time =  datetime.datetime.now()
    n = 5000000000 # One billion; Adjust as Accordingly
    init_sieve(n)
    n_list = range(24, int(n**0.5) + 1)
    thread_sieve(n_list)

    print(f"There are {len([x for x in range(n + 1) if global_sieve[x]])} primes in 5 billion")
    finish_time =  datetime.datetime.now()
    duration = finish_time - start_time
    print(f"Start Time: {start_time}")
    print(f"Finish Time: {finish_time}")
    print(f"Duration: {duration}")
