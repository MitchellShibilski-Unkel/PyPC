import time


# Start timer
startTimer = time.perf_counter()
startTimer2 = time.process_time()

# Random numbers in a list
theList = [4, 5, 1, 3, 6, 10, 8, 9, 11, 7, 20, 22, 13, 17, 18, 12, 16, 71]

# Run sort
print(theList.sort())

endTimer = time.perf_counter()
endTimer2 = time.process_time()

print(f"Task Finished In Performance: {endTimer - startTimer:0.8f}\nTask Finished In Process/CPU/Kernel + User Space: {endTimer2 - startTimer2:0.8f}")