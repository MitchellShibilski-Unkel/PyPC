from Sorting_Tests import bubbleSort, greatestAndLeastSort, mergeSort, selectionSort
import time

def sortingTest(listInput):
    startTimer = time.process_time()
    startTimer2 = time.process_time()
    
    bubbleSort.bubbleSort(listInput)
    
    endTimer2 = time.process_time()
    
    startTimer3 = time.process_time()
    
    greatestAndLeastSort.gtolSort(listInput)
    
    endTimer3 = time.process_time()
    
    startTimer4 = time.process_time()
    
    mergeSort.mergeSort(listInput)
    
    endTimer4 = time.process_time()
    
    startTimer5 = time.process_time()
    
    selectionSort.selectionSort(listInput)
    
    endTimer5 = time.process_time()
    endTimer = time.process_time()
    
    pointList = []
    
    pointList.append((endTimer2 - startTimer2) * 0.0005 // 10)
    pointList.append((endTimer3 - startTimer3) * 0.0005 // 10)
    pointList.append((endTimer4 - startTimer4) * 0.0005 // 10)
    pointList.append((endTimer5 - startTimer5) * 0.0005 // 10)
    
    points = sum(pointList)
    
    if points == 0:
        points = 2
    elif points <= 1 and points > 0:
        points = 1
    else:
        points = 0
    
    pointList.append(points + (endTimer - startTimer) // 10)
    
    return pointList[-1]