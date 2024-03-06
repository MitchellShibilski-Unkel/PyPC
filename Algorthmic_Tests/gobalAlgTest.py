from Algorthmic_Tests import primeCounter
from Algorthmic_Tests import waveFunction
import time


def algorithmTest():
    startTimer = time.process_time()
    startTimer2 = time.process_time()
    
    hundred = primeCounter.primeCounter(101) 
    
    endTimer2 = time.process_time()
    
    startTimer3 = time.process_time()
    
    thousand = primeCounter.primeCounter(1001)
    
    endTimer3 = time.process_time()
    
    startTimer4 = time.process_time()
    
    tenthousand = primeCounter.primeCounter(10001)
    
    endTimer4 = time.process_time()
    
    startTimer5 = time.process_time()
    
    waveFunction.waveFunc(1000)
    
    endTimer5 = time.process_time()
    
    endTimer = time.process_time()
    
    pointList = []
    
    pointList.append((endTimer2 - startTimer2) // 0.0005 * 0.1)
    pointList.append((endTimer3 - startTimer3) // 0.0005 * 0.1)
    pointList.append((endTimer4 - startTimer4) // 0.0005 * 0.1)
    pointList.append((endTimer5 - startTimer5) // 0.0005 * 0.1)
    pointList.append(sum(pointList) + (endTimer - startTimer) // 10)
    
    return pointList[-1]