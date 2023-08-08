import datetime
def amazon_primes(primes, n):
    amazon_primes = primes
    for i in range(10, n):
        for j in primes:
            if i % j == 0:
                primes.append(i)
                #print(i)
                break
    return primes
start_time =  datetime.datetime.now()
primes = [1,2,3,5,7]
primes = amazon_primes(primes, 1000000000)
print(primes)
finish_time =  datetime.datetime.now()
duration = finish_time - start_time
print(f"Start Time: {start_time}")
print(f"Finish Time: {finish_time}")
print(f"Duration: {duration}")