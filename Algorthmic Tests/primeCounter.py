import time
import numpy as np


# --- Prime Function --- #
primeList = []
def primeCounter(countUpTo):
    list = [x for x in range(0,countUpTo)]

    # Get the value in the list
    for i in range(len(list)):
        # From 2 to the value, check to see if it is a prime; if the remainder is zero, not a prime; else, append prime number to the primeList
        for k in range(2, i):
            if i % k == 0:
                break
        else:
            primeList.append(i)

    print(primeList)

# --- Primes to 100 --- #
# Start timer
startTimer = time.perf_counter()
startTimer2 = time.process_time()

primeCounter(101)
    
endTimer = time.perf_counter()
endTimer2 = time.process_time()

print(f"Task Finished In Performance: {endTimer - startTimer:0.8f}s\nTask Finished In Process/CPU/Kernel + User Space: {endTimer2 - startTimer2:0.8f}s")

# --- Primes to 1000 --- #
# Start timer
startTimer = time.perf_counter()
startTimer2 = time.process_time()

primeCounter(1001)
    
endTimer = time.perf_counter()
endTimer2 = time.process_time()

print(f"Task Finished In Performance: {endTimer - startTimer:0.8f}s\nTask Finished In Process/CPU/Kernel + User Space: {endTimer2 - startTimer2:0.8f}s")

# --- Primes to 10000 --- #
# Start timer
startTimer = time.perf_counter()
startTimer2 = time.process_time()

primeCounter(10001)
    
endTimer = time.perf_counter()
endTimer2 = time.process_time()

print(f"Task Finished In Performance: {endTimer - startTimer:0.8f}s\nTask Finished In Process/CPU/Kernel + User Space: {endTimer2 - startTimer2:0.8f}s")

# --- Primes to 1000000 --- #
# Start timer
startTimer = time.perf_counter()
startTimer2 = time.process_time()

primeCounter(1000001)
    
endTimer = time.perf_counter()
endTimer2 = time.process_time()

print(f"Task Finished In Performance: {endTimer - startTimer:0.8f}s\nTask Finished In Process/CPU/Kernel + User Space: {endTimer2 - startTimer2:0.8f}s")