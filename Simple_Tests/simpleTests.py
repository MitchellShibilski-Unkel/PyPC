from Simple_Tests import allBasicMath, forBreakTest, forTest
import time


def simpleTest(listInput, num1, num2):
    startTimer = time.process_time()
    startTimer2 = time.process_time()
    
    allBM = allBasicMath.math(num1, num2)
    
    endTimer2 = time.process_time()
    
    startTimer3 = time.process_time()
    
    for1 = forTest.forLoop(listInput)
    
    endTimer3 = time.process_time()
    
    startTimer4 = time.process_time()
    
    for2 = forBreakTest.forLoop(listInput)
    
    endTimer4 = time.process_time()
    
    endTimer = time.process_time()
    
    pointList = []
    
    pointList.append((endTimer2 - startTimer2) * 0.0005)
    pointList.append((endTimer3 - startTimer3) * 0.0005)
    pointList.append((endTimer4 - startTimer4) * 0.0005)
    
    points = sum(pointList)
    
    if points == 0:
        points = 1
    else:
        points = 0
    
    pointList.append(points + (endTimer - startTimer) * 0.1)
    
    return pointList[-1]