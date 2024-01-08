import time


# Start timer
startTimer = time.perf_counter()
startTimer2 = time.process_time()

# List to cycle through
theList = ["a", "b", "i", "c", "d", "e", "n", "h", "j", ".", "m", "n", "l", "o", "t", "."]

# Start "for" loop to separate values in the list, theList
separation = "."
tempList = []
finalList = []
for i in theList:
    if i == ".":
        tempList.append(i)
        finalList.append(tempList)
        tempList = []
    else:
        tempList.append(i)
        
# Append tempList to finalList
finalList.append(tempList)

endTimer = time.perf_counter()
endTimer2 = time.process_time()

print(f"Task Finished In Performance: {endTimer - startTimer:0.8f}s\nTask Finished In Process/CPU/Kernel + User Space: {endTimer2 - startTimer2:0.8f}s")