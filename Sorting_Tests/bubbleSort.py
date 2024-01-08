import time


# Start timer
startTimer = time.perf_counter()
startTimer2 = time.process_time()

# Random numbers in a list
theList = [None]

# Run sort
print(theList.sort())

endTimer = time.perf_counter()
endTimer2 = time.process_time()

print(f"Task Finished In Performance: {endTimer - startTimer:0.8f}s\nTask Finished In Process/CPU/Kernel + User Space: {endTimer2 - startTimer2:0.8f}s")