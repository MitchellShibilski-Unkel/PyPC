import random
import time


# Start timer
startTimer = time.perf_counter()
startTimer2 = time.process_time()

# Getting numbers
fNum = random.randint(0, 9)
sNum = random.randint(0, 9)
    
# ---- Do math ----#
def math(a, b): 
    # Add
    addValue = int(a + b)

    # Subtract
    subValue = int(a - b)

    # Multiply
    multValue = int(a * b)

    # Divide
    if a == 0 or sNum == 0:
        divideValue = 0
    else:
        divideValue = float(a / b)

    print(addValue, subValue, multValue, divideValue)
    
endTimer = time.perf_counter()
endTimer2 = time.process_time()

print(f"Task Finished In Performance: {endTimer - startTimer:0.8f}s\nTask Finished In Process/CPU/Kernel + User Space: {endTimer2 - startTimer2:0.8f}s")