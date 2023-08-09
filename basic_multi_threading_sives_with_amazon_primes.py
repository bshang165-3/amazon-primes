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
n = 1000000000 # One billion; Adjust as Accordingly
global_sieve = [True] * (n + 1)
print("n is one billion; adjust as accordingly", n)
global_sieve = [True] * (n + 1)
global_sieve[0] = global_sieve[1] = False 
i = 2
global_sieve[i*i: n+1: i] = [False] * len(range(i*i, n+1, i))

def add_to_primes(item):
    global global_primes 
    global_primes.append(item)

def print_primes():
    global global_primes 
    print("Global Primes:", global_primes)

# def change_to_false(i):
#     global global_sieve
#     for i in range(i, len(global_sieve), i):
#         global_sieve[i] = False

def if_sieve(i):
    k = i
    if global_sieve[i] and is_prime(k):
        add_to_primes(i)
        #print('found prime', i)
        print(f"Marking all multiples of {i} as non-primes")
        # change_to_false(i)
        global_sieve[i*i: n+1: i] = [False] * len(range(i*i, n+1, i))
        # time.sleep(1)

def is_prime(i):
    for j in global_primes:
        if i % j == 0:
            return False
    return True


def thread_sieve(thread_list, max_threads=2):
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_threads) as executor:
        futures = [executor.submit(if_sieve, i) for i in thread_list]
        concurrent.futures.wait(futures)

if __name__ == "__main__":
    start_time =  datetime.datetime.now()
    n_list = range(3, int(n**0.5) + 1)
    thread_sieve(n_list)

    #print([x for x in range(n + 1) if sieve[x]])
    print(f"There are {len([x for x in range(n + 1) if global_sieve[x]])} primes in one billion")
    finish_time =  datetime.datetime.now()
    duration = finish_time - start_time
    print(f"Start Time: {start_time}")
    print(f"Finish Time: {finish_time}")
    print(f"Duration: {duration}")
