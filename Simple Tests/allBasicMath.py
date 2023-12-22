import random
import time


# Start timer
startTimer = time.perf_counter()
startTimer2 = time.process_time()

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
if fNum == 0 or sNum == 0:
    divideValue = 0
else:
    divideValue = float(fNum / sNum)

print(addValue, subValue, multValue, divideValue)
    
endTimer = time.perf_counter()
endTimer2 = time.process_time()

print(f"Task Finished In Performance: {endTimer - startTimer:0.8f}s\nTask Finished In Process/CPU/Kernel + User Space: {endTimer2 - startTimer2:0.8f}s")