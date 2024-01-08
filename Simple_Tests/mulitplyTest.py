import random
import time


# Start timer
startTimer = time.perf_counter()
startTimer2 = time.process_time()

# Getting numbers
fNum = random.randint(0, 9)
sNum = random.randint(0, 9)
    
# Multiply num
finalValue = int(fNum * sNum)

print(finalValue)
    
endTimer = time.perf_counter()
endTimer2 = time.process_time()

print(f"Task Finished In Performance: {endTimer - startTimer:0.8f}s\nTask Finished In Process/CPU/Kernel + User Space: {endTimer2 - startTimer2:0.8f}s")