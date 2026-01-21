import time
from AI.aiTests import *
from General_Computer_Info.generalSpecs import CPUsage, RAMUsage

def traningRNNModelRunner(dataset: tuple = (None, None), epochs: int = 50, device: str = "cpu", inputSize: int = 16, hx: int = 32):
    startTimer = time.process_time()
    
    training = TrainRNNModel(dataset[0], dataset[1], epochs=epochs, device="cpu")
    run = training.run(inputSize=inputSize, hx=hx)

    endTimer = time.process_time()

    totalTime = (endTimer - startTimer)
    
    return str(f"Your AI Training Took: {totalTime}s\n{CPUsage()}\n{RAMUsage()}")