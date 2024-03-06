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