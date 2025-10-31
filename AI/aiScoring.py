import time
from AI.aiTests import *


def score(_in, device, test: int = 1, inputSize: int = 16, hx: int = 32, outputSize: int = 1, numLayers: int = 24, model = "google/gemma-3-270m", type: str = "text-generation"):
    startTimer = time.perf_counter()
    startTimer2 = time.process_time()
    
    change = 0 # Placeholder for HuggingFace
    
    if test == 1:
        SimpleNeuralNet(inputSize, hx, outputSize).to(device)(_in)
    elif test == 2:
        RNN(inputSize, hx, outputSize, numLayers).to(device)(_in)
    elif test == 3:
        LargeNeuralNet(inputSize, hx, outputSize, numLayers).to(device)(_in)
    elif test == 4:
        HuggingFace(model, device, type).model(_in)
        change = 100
    else:
        SimpleNeuralNet(inputSize, hx, outputSize).to(device)(_in)
        
    endTimer = time.perf_counter()
    endTimer2 = time.process_time()
    
    totalTime = (endTimer - startTimer) + (endTimer2 - startTimer2)
    points = (1000 // totalTime * 0.1) + change
    return f"AI Score: {points} | Time Taken: {totalTime}s"