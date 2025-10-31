from Algorthmic_Tests import gobalAlgTest
from Simple_Tests import simpleTests
from Sorting_Tests import sortingTest
from General_Computer_Info import generalSpecs
from WiFi_Test import wifi
from AI.aiScoring import *
import time
import numpy as np
import random
from torch import tensor

def terminal(l = [], a = 0, b = 0, l2 = []):
    typeOfTest = input("AI Tests [y/n]: ")    
    if typeOfTest.lower() == "y":
        whichAI = input("Which AI Test? (SimpleNeuralNet [or 1]/RNN [or 2]/LargeNeuralNet [or 3]/HuggingFace [or 4]): ")
        if whichAI != "HuggingFace" and whichAI != "4":
            minDataPoint = int(input("Minimum Data Points (Default 16): ") or "16")
            maxDataPoint = int(input("Maximum Data Points (Default 1024): ") or "1024")
            inputSize = int(input("Input Size (Default 16): ") or "16")
            hx = int(input("Hidden Layer Size (Default 32): ") or "32")
            outputSize = int(input("Output Size (Default 1): ") or "1")
            numLayers = int(input("Number of Layers (Default 24): ") or "24")
            
        try:
            if minDataPoint == None:
                minDataPoint = 16
            if maxDataPoint == None:
                maxDataPoint = 1024
            if inputSize == None:
                inputSize = 16
        except UnboundLocalError:
            minDataPoint = 16
            maxDataPoint = 1024
            inputSize = 16
            
        device = input("Device (cpu/cuda/xpu/vulkan/mps) (Default cpu): ") or "cpu"
        data = np.random.rand(random.randint(minDataPoint, maxDataPoint), inputSize).astype(np.float32)
        data = tensor(data).to(device)
        
        if whichAI == "SimpleNeuralNet" or whichAI == "1":
            return score(data, device, test=1, inputSize=inputSize, hx=hx, outputSize=outputSize)
        elif whichAI == "RNN" or whichAI == "2":
            return score(data, device, test=2, inputSize=inputSize, hx=hx, outputSize=outputSize, numLayers=numLayers)
        elif whichAI == "LargeNeuralNet" or whichAI == "3":
            return score(data, device, test=3, inputSize=inputSize, hx=hx, outputSize=outputSize, numLayers=numLayers)
        elif whichAI == "HuggingFace" or whichAI == "4":
            usePrompt = input("Use a Custom Prompt? [y/n]: ")
            if usePrompt == "y":
                prompt = input("Enter Your Prompt [string/list]: ")
                data = prompt
            modelName = input("HuggingFace Model Name (Default google/gemma-3-270m): ") or "google/gemma-3-270m"
            modelType = input("HuggingFace Model Type (Default text-generation): ") or "text-generation"
            return score(data, device, test=4, inputSize=inputSize, hx=0, outputSize=1, model=modelName, type=modelType)
        else:
            return score(data, device, test=1, inputSize=inputSize, hx=hx, outputSize=outputSize)
    else:
        startTimer = time.process_time()
    
        alg = gobalAlgTest.algorithmTest()
        sim = simpleTests.simpleTest(l, a, b)
        s = sortingTest.sortingTest(l2)
        w = wifi.speedTest()

        endTimer = time.process_time()

        totalTime = (endTimer - startTimer)
        totalPoints = (alg + sim + s + w) // totalTime * 0.1
        
        return str(f"Your {generalSpecs.CPU()} Has A Total Points Of: {np.round(totalPoints, 2)} | Total Time: {totalTime}s | Algorithm Test Points: {alg} | Simple Test Points: {sim} | Sorting Test Points: {s} | WiFi Test Points: {w}")

l = ["a", "b", "i", "c", "d", ".", "n", ".", "j", ".", "m", "n", "l", "o", "t", ".", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", ".", "q", "r", "s", "t", ";", ".", "w", "x", "y", "z"]
a = random.randint(0, 100000000)
b = random.randint(0, 100000000)
l2 = [random.randint(0, 100000000) for _ in range(random.randrange(8, 10000))]

def run():
    return terminal(l, a, b, l2)

print(run())
