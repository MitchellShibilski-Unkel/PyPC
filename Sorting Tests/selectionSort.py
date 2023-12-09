import time


# Start timer
startTimer = time.perf_counter()
startTimer2 = time.process_time()

listOfNums = [None]

# --- Selection Sort --- #
sortedList = []
def selectionSort(array = []):
    i = 0
    for arr in range(len(array)):
        if i == len(array):
            i = 0
            break
        else:
            arrMin = min(array)
            i += 1
            sortedList.append(arrMin)
            listOfNums.remove(arrMin)

# Give list to the func/algorithm          
selectionSort(listOfNums)

print(sortedList)
    
endTimer = time.perf_counter()
endTimer2 = time.process_time()

print(f"Task Finished In Performance: {endTimer - startTimer:0.8f}\nTask Finished In Process/CPU/Kernel + User Space: {endTimer2 - startTimer2:0.8f}")