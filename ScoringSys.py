from Algorthmic_Tests import gobalAlgTest
from Simple_Tests import simpleTests
from Sorting_Tests import sortingTest
from General_Computer_Info import generalSpecs
import time
import numpy as np

def allTests(l = [], a = 0, b = 0, l2 = []):
    startTimer = time.process_time()
    
    alg = gobalAlgTest.algorithmTest()
    sim = simpleTests.simpleTest(l, a, b)
    s = sortingTest.sortingTest(l2)

    endTimer = time.process_time()

    totalTime = (endTimer - startTimer)
    
    totalPoints = (alg + sim + s) // totalTime * 0.1
    
    return str(f"Your {generalSpecs.CPU()} Has A Total Points Of: {np.round(totalPoints, 2)} | Total Time: {totalTime}s | Algorithm Test Points: {alg} | Simple Test Points: {sim} | Sorting Test Points: {s}")