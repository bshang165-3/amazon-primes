# Multi-threading Sieve of Eratosthenes
import threading
import datetime
import pickle
import concurrent.futures
import sys
# current_limit = sys.getrecursionlimit()
# print("Current recursion limit:", current_limit)
#sys.exit()
sys.setrecursionlimit(1000000000)

def if_sieve(i):
    if sieve[i]:
        print(f"Marking all multiples of {i} as non-primes")
        j = 1
        while j * i < len(sieve):
            sieve[i*j] = False
            j += 1
        #sieve[i*i: n+1: i] = [False] * len(range(i*i, n+1, i))
        thread_list = range(i+1, i*2-1)
        thread_sieve(thread_list)
        # for _ in range(i+1, i*2-1):
        #     if sieve[_]:
        #         y = threading.Thread(target=if_sieve(_), daemon=True)
        #         y.start()
        #         y.join()

def thread_sieve(thread_list, max_threads=10000):
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_threads) as executor:
        futures = [executor.submit(if_sieve, i) for i in thread_list]
        concurrent.futures.wait(futures)

if __name__ == "__main__":
    start_time =  datetime.datetime.now()
    n = 1000000000 # Ten billion; Adjust as Accordingly
    print("n is ten billion; adjust as accordingly", n)
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False 
    n_list = range(2, int(n**0.5) + 1)
    thread_sieve(n_list)
    # for i in n_list:
    #     if_sieve(i)
        # x = threading.Thread(target=if_sieve(i), daemon=True)
        # x.start()

    print([x for x in range(n + 1) if sieve[x]])
    print(f"There are {len([x for x in range(n + 1) if sieve[x]])} primes in 10 billion")

    finish_time =  datetime.datetime.now()
    duration = finish_time - start_time
    print(f"Start Time: {start_time}")
    print(f"Finish Time: {finish_time}")
    print(f"Duration: {duration}")
