import time


# Start timer
startTimer = time.perf_counter()
startTimer2 = time.process_time()

# List to cycle through
theList = ["a", "b", "i", "c", "d", "e", "n", "h", "j", ".", "m", "n", "l", "o", "t", "."]

# Start "for" loop
def forLoop(l):
    for i in l:
        if i != ".":
            continue
        else:
            print(i)
            break
        
forLoop(theList)

endTimer = time.perf_counter()
endTimer2 = time.process_time()

print(f"Task Finished In Performance: {endTimer - startTimer:0.8f}s\nTask Finished In Process/CPU/Kernel + User Space: {endTimer2 - startTimer2:0.8f}s")