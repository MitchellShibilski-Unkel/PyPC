import random
import time


# Start timer
startTimer = time.perf_counter()

# Getting numbers
fNum = random.randint(0, 9)
sNum = random.randint(0, 9)
    
# Multiply num
finalValue = int(fNum * sNum)

print(finalValue)
    
endTimer = time.perf_counter()

print(f"Finished Task In: {endTimer - startTimer:0.4f}s")