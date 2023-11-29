import time


# Start timer
startTimer = time.perf_counter()
startTimer2 = time.process_time()

# List to cycle through
theList = ["a", "b", "i", "c", "d", "e", "n", "h", "j", ".", "m", "n", "l", "o", "t", "."]

# Start "for" loop
for i in theList:
    if i != ".":
        continue
    else:
        print(i)
        break

endTimer = time.perf_counter()
endTimer2 = time.process_time()

print(f"Task Finished In Performance: {endTimer - startTimer:0.8f}\nTask Finished In Process/CPU/Kernel + User Space: {endTimer2 - startTimer2:0.8f}")