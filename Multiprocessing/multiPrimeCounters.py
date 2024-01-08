import time
import multiprocessing as mp
from Algorthmic_Tests import primeCounter


def multiPrimeCounting(numOfCores = 6, countTo = 1001):
    counter = primeCounter.primeCounter(countTo)

    if numOfCores == 3:
        p1 = mp.Process(target=counter).start()
        p2 = mp.Process(target=counter).start()
        p3 = mp.Process(target=counter).start()
    elif numOfCores == 4:
        p1 = mp.Process(target=counter).start()
        p2 = mp.Process(target=counter).start()
        p3 = mp.Process(target=counter).start()
        p4 = mp.Process(target=counter).start()
    elif numOfCores == 5:
        p1 = mp.Process(target=counter).start()
        p2 = mp.Process(target=counter).start()
        p3 = mp.Process(target=counter).start()
        p4 = mp.Process(target=counter).start()
        p5 = mp.Process(target=counter).start()
    elif numOfCores == 6:
        p1 = mp.Process(target=counter).start()
        p2 = mp.Process(target=counter).start()
        p3 = mp.Process(target=counter).start()
        p4 = mp.Process(target=counter).start()
        p5 = mp.Process(target=counter).start()
        p6 = mp.Process(target=counter).start()
    elif numOfCores == 8:
        p1 = mp.Process(target=counter).start()
        p2 = mp.Process(target=counter).start()
        p3 = mp.Process(target=counter).start()
        p4 = mp.Process(target=counter).start()
        p5 = mp.Process(target=counter).start()
        p6 = mp.Process(target=counter).start()
        p7 = mp.Process(target=counter).start()
        p8 = mp.Process(target=counter).start()
    elif numOfCores == 10:
        p1 = mp.Process(target=counter).start()
        p2 = mp.Process(target=counter).start()
        p3 = mp.Process(target=counter).start()
        p4 = mp.Process(target=counter).start()
        p5 = mp.Process(target=counter).start()
        p6 = mp.Process(target=counter).start()
        p7 = mp.Process(target=counter).start()
        p8 = mp.Process(target=counter).start()
        p9 = mp.Process(target=counter).start()
        p10 = mp.Process(target=counter).start()
    elif numOfCores == 12:
        p1 = mp.Process(target=counter).start()
        p2 = mp.Process(target=counter).start()
        p3 = mp.Process(target=counter).start()
        p4 = mp.Process(target=counter).start()
        p5 = mp.Process(target=counter).start()
        p6 = mp.Process(target=counter).start()
        p7 = mp.Process(target=counter).start()
        p8 = mp.Process(target=counter).start()
        p9 = mp.Process(target=counter).start()
        p10 = mp.Process(target=counter).start()
        p11 = mp.Process(target=counter).start()
        p12 = mp.Process(target=counter).start()
    elif numOfCores == 14:
        p1 = mp.Process(target=counter).start()
        p2 = mp.Process(target=counter).start()
        p3 = mp.Process(target=counter).start()
        p4 = mp.Process(target=counter).start()
        p5 = mp.Process(target=counter).start()
        p6 = mp.Process(target=counter).start()
        p7 = mp.Process(target=counter).start()
        p8 = mp.Process(target=counter).start()
        p9 = mp.Process(target=counter).start()
        p10 = mp.Process(target=counter).start()
        p11 = mp.Process(target=counter).start()
        p12 = mp.Process(target=counter).start()
        p13 = mp.Process(target=counter).start()
        p14 = mp.Process(target=counter).start()
    elif numOfCores == 16:
        p1 = mp.Process(target=counter).start()
        p2 = mp.Process(target=counter).start()
        p3 = mp.Process(target=counter).start()
        p4 = mp.Process(target=counter).start()
        p5 = mp.Process(target=counter).start()
        p6 = mp.Process(target=counter).start()
        p7 = mp.Process(target=counter).start()
        p8 = mp.Process(target=counter).start()
        p9 = mp.Process(target=counter).start()
        p10 = mp.Process(target=counter).start()
        p11 = mp.Process(target=counter).start()
        p12 = mp.Process(target=counter).start()
        p13 = mp.Process(target=counter).start()
        p14 = mp.Process(target=counter).start()
        p15 = mp.Process(target=counter).start()
        p16 = mp.Process(target=counter).start()
    elif numOfCores == 18:
        p1 = mp.Process(target=counter).start()
        p2 = mp.Process(target=counter).start()
        p3 = mp.Process(target=counter).start()
        p4 = mp.Process(target=counter).start()
        p5 = mp.Process(target=counter).start()
        p6 = mp.Process(target=counter).start()
        p7 = mp.Process(target=counter).start()
        p8 = mp.Process(target=counter).start()
        p9 = mp.Process(target=counter).start()
        p10 = mp.Process(target=counter).start()
        p11 = mp.Process(target=counter).start()
        p12 = mp.Process(target=counter).start()
        p13 = mp.Process(target=counter).start()
        p14 = mp.Process(target=counter).start()
        p15 = mp.Process(target=counter).start()
        p16 = mp.Process(target=counter).start()
        p17 = mp.Process(target=counter).start()
        p18 = mp.Process(target=counter).start()
    else:
        pass

# Start timer
startTimer = time.perf_counter()
startTimer2 = time.process_time()
    
# Start prime counter
multiPrimeCounting(numOfCores, countTo)

endTimer = time.perf_counter()
endTimer2 = time.process_time()

print(f"Task Finished In Performance: {endTimer - startTimer:0.8f}s\nTask Finished In Process/CPU/Kernel + User Space: {endTimer2 - startTimer2:0.8f}s")