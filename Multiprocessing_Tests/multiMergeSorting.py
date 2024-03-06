import time
import multiprocessing as mp
from Sorting_Tests import mergeSort


# List to sort
list = [nums]

def multiMergeSorting(numOfCores = 6):
    sort = mergeSort.mergeSort(list)

    if numOfCores == 3:
        p1 = mp.Process(target=sort).start()
        p2 = mp.Process(target=sort).start()
        p3 = mp.Process(target=sort).start()
    elif numOfCores == 4:
        p1 = mp.Process(target=sort).start()
        p2 = mp.Process(target=sort).start()
        p3 = mp.Process(target=sort).start()
        p4 = mp.Process(target=sort).start()
    elif numOfCores == 5:
        p1 = mp.Process(target=sort).start()
        p2 = mp.Process(target=sort).start()
        p3 = mp.Process(target=sort).start()
        p4 = mp.Process(target=sort).start()
        p5 = mp.Process(target=sort).start()
    elif numOfCores == 6:
        p1 = mp.Process(target=sort).start()
        p2 = mp.Process(target=sort).start()
        p3 = mp.Process(target=sort).start()
        p4 = mp.Process(target=sort).start()
        p5 = mp.Process(target=sort).start()
        p6 = mp.Process(target=sort).start()
    elif numOfCores == 8:
        p1 = mp.Process(target=sort).start()
        p2 = mp.Process(target=sort).start()
        p3 = mp.Process(target=sort).start()
        p4 = mp.Process(target=sort).start()
        p5 = mp.Process(target=sort).start()
        p6 = mp.Process(target=sort).start()
        p7 = mp.Process(target=sort).start()
        p8 = mp.Process(target=sort).start()
    elif numOfCores == 10:
        p1 = mp.Process(target=sort).start()
        p2 = mp.Process(target=sort).start()
        p3 = mp.Process(target=sort).start()
        p4 = mp.Process(target=sort).start()
        p5 = mp.Process(target=sort).start()
        p6 = mp.Process(target=sort).start()
        p7 = mp.Process(target=sort).start()
        p8 = mp.Process(target=sort).start()
        p9 = mp.Process(target=sort).start()
        p10 = mp.Process(target=sort).start()
    elif numOfCores == 12:
        p1 = mp.Process(target=sort).start()
        p2 = mp.Process(target=sort).start()
        p3 = mp.Process(target=sort).start()
        p4 = mp.Process(target=sort).start()
        p5 = mp.Process(target=sort).start()
        p6 = mp.Process(target=sort).start()
        p7 = mp.Process(target=sort).start()
        p8 = mp.Process(target=sort).start()
        p9 = mp.Process(target=sort).start()
        p10 = mp.Process(target=sort).start()
        p11 = mp.Process(target=sort).start()
        p12 = mp.Process(target=sort).start()
    elif numOfCores == 14:
        p1 = mp.Process(target=sort).start()
        p2 = mp.Process(target=sort).start()
        p3 = mp.Process(target=sort).start()
        p4 = mp.Process(target=sort).start()
        p5 = mp.Process(target=sort).start()
        p6 = mp.Process(target=sort).start()
        p7 = mp.Process(target=sort).start()
        p8 = mp.Process(target=sort).start()
        p9 = mp.Process(target=sort).start()
        p10 = mp.Process(target=sort).start()
        p11 = mp.Process(target=sort).start()
        p12 = mp.Process(target=sort).start()
        p13 = mp.Process(target=sort).start()
        p14 = mp.Process(target=sort).start()
    elif numOfCores == 16:
        p1 = mp.Process(target=sort).start()
        p2 = mp.Process(target=sort).start()
        p3 = mp.Process(target=sort).start()
        p4 = mp.Process(target=sort).start()
        p5 = mp.Process(target=sort).start()
        p6 = mp.Process(target=sort).start()
        p7 = mp.Process(target=sort).start()
        p8 = mp.Process(target=sort).start()
        p9 = mp.Process(target=sort).start()
        p10 = mp.Process(target=sort).start()
        p11 = mp.Process(target=sort).start()
        p12 = mp.Process(target=sort).start()
        p13 = mp.Process(target=sort).start()
        p14 = mp.Process(target=sort).start()
        p15 = mp.Process(target=sort).start()
        p16 = mp.Process(target=sort).start()
    elif numOfCores == 18:
        p1 = mp.Process(target=sort).start()
        p2 = mp.Process(target=sort).start()
        p3 = mp.Process(target=sort).start()
        p4 = mp.Process(target=sort).start()
        p5 = mp.Process(target=sort).start()
        p6 = mp.Process(target=sort).start()
        p7 = mp.Process(target=sort).start()
        p8 = mp.Process(target=sort).start()
        p9 = mp.Process(target=sort).start()
        p10 = mp.Process(target=sort).start()
        p11 = mp.Process(target=sort).start()
        p12 = mp.Process(target=sort).start()
        p13 = mp.Process(target=sort).start()
        p14 = mp.Process(target=sort).start()
        p15 = mp.Process(target=sort).start()
        p16 = mp.Process(target=sort).start()
        p17 = mp.Process(target=sort).start()
        p18 = mp.Process(target=sort).start()
    else:
        pass

# Start timer
startTimer = time.perf_counter()
startTimer2 = time.process_time()

multiMergeSorting(numOfCores)

endTimer = time.perf_counter()
endTimer2 = time.process_time()

print(f"Task Finished In Performance: {endTimer - startTimer:0.8f}s\nTask Finished In Process/CPU/Kernel + User Space: {endTimer2 - startTimer2:0.8f}s")