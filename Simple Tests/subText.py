import random
import time


# Start timer
startTimer = time.perf_counter()

# Getting numbers
fNum = random.randint(0, 9)
sNum = random.randint(0, 9)
    
# Subtract num
if fNum > sNum:
    finalValue = int(fNum - sNum)
else:
    finalValue = int(sNum - fNum)

print(finalValue)
    
endTimer = time.perf_counter()

print(f"Finished Task In: {endTimer - startTimer:0.8f}s")