import datetime
import concurrent.futures

def amazon_primes(primes, n):
    for i in range(10, n):
        pt = True
        for j in primes:
            if i % j == 0:
                pt = False
                break
            else:
                continue
        if pt == True:
            primes.append(i)
    return primes
start_time =  datetime.datetime.now()

primes = [2,3,5,7]
primes = amazon_primes(primes, 1000000)

print(primes)

print(f"there are {len(primes)} from 0 to 1M")

finish_time =  datetime.datetime.now()
duration = finish_time - start_time
print(f"Start Time: {start_time}")
print(f"Finish Time: {finish_time}")
print(f"Duration of Amazon Primes 1M is: {duration}")