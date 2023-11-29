import random
import time


# Start timer
startTimer = time.perf_counter()

# Getting numbers
fNum = random.randint(0, 9)
sNum = random.randint(0, 9)
    
# ---- Do math ----#
# Add
addValue = int(fNum + sNum)

# Subtract
subValue = int(fNum - sNum)

# Multiply
multValue = int(fNum * sNum)

# Divide
divideValue = float(fNum / sNum)

print(addValue, subValue, multValue, divideValue)
    
endTimer = time.perf_counter()

print(f"Finished Task In: {endTimer - startTimer:0.4f}s")