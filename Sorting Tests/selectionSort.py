import time


# Start timer
startTimer = time.perf_counter()
startTimer2 = time.process_time()

listOfNums = [None]

# --- Selection Sort --- #
sortedList = []
def selectionSort(array = []):
    for arr in range(len(array)):
        arrMin = min(array)
        sortedList.append(arrMin)
        listOfNums.remove(arrMin)

# Give list to the func/algorithm          
selectionSort(listOfNums)

print(sortedList)
    
endTimer = time.perf_counter()
endTimer2 = time.process_time()

print(f"Task Finished In Performance: {endTimer - startTimer:0.8f}\nTask Finished In Process/CPU/Kernel + User Space: {endTimer2 - startTimer2:0.8f}")