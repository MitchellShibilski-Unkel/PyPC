import time


# Start timer
startTimer = time.perf_counter()
startTimer2 = time.process_time()

# Random numbers in a list
theList = []

# --- Merge Sort --- #
sortedList = []
def mergeSort(array = []):  
    # Get each side their vars  
    leftSum = len(array) // 2
    leftSide = array[0:leftSum]
    rightSide = array[leftSum:]
    
    sortedArray = []

    # Register values as a functional list
    newRightSideList = []    
    newLeftSideList = []
    for nl in leftSide:
        newLeftSideList.append(nl)
    for rl in rightSide:
        newRightSideList.append(rl)

    # Sort left side
    for l in range(len(newLeftSideList)):
        minValue = min(newLeftSideList)
        sortedArray.append(minValue)
        newLeftSideList.remove(minValue)
    
    # Sort right side
    for r in range(len(newRightSideList)):
        minValue = min(newRightSideList)
        sortedArray.append(minValue)
        newRightSideList.remove(minValue)

    # Sorted list
    # Finally, sort both sides using each sorted side (left and right)
    print(sorted(sortedArray))
    
mergeSort(theList)

endTimer = time.perf_counter()
endTimer2 = time.process_time()

print(f"Task Finished In Performance: {endTimer - startTimer:0.8f}s\nTask Finished In Process/CPU/Kernel + User Space: {endTimer2 - startTimer2:0.8f}s")