# PyPC - Python PC Performance Tests

A comprehensive Python-based benchmarking tool that tests your computer's performance across multiple domains, including CPU, AI/ML workloads, algorithmic challenges, sorting operations, and network speed.

## Features

- **AI/ML Benchmarks**: Test neural networks locally on CPU, GPU (CUDA), XPU, MPS, and Vulkan
- **Algorithmic Tests**: Complex computational challenges including wave functions and prime counting
- **Sorting Algorithms**: Multiple sorting implementations with performance metrics
- **Multiprocessing Tests**: Stress test your CPU with parallel workloads
- **Network Speed Testing**: WiFi upload/download speed measurements
- **System Information**: Comprehensive CPU, RAM, and system specifications

## Installation

### Method 1: Install from GitHub
```bash
pip install git+https://github.com/MitchellShibilski-Unkel/PyPC.git@main
```

### Method 2: Install from Source
1. Clone the repository
```bash
git clone https://github.com/MitchellShibilski-Unkel/PyPC.git
cd PyPC
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

### Required Dependencies
```
torch
transformers
numpy
psutil
py-cpuinfo
speedtest-cli
```

## Quick Start

### Command Line Interface
Run the interactive terminal interface:
```bash
python ScoringSysCMD.py
```

### Python API
```python
from ScoringSys import allTestsExpectAI
from General_Computer_Info import generalSpecs

# Run all tests (excluding AI)
l = ["a", "b", "c", "d", "e", "f"]
a = 1000
b = 2000
l2 = [5, 2, 8, 1, 9, 3, 7, 4, 6]

result = allTestsExpectAI(l, a, b, l2)
print(result)

# Get system specs
print(generalSpecs.CPU())
print(generalSpecs.RAMUsage())
```

## Test Categories

### 1. Simple Tests
Basic computational operations and loop performance:
- **Math Operations**: Addition, subtraction, multiplication, division
- **Loop Tests**: For loop iterations with break conditions
- **List Processing**: Array manipulation and filtering

### 2. Sorting Algorithms
Test various sorting implementations:
- **Selection Sort**: Least-to-greatest and greatest-to-least
- **Merge Sort**: Divide-and-conquer sorting
- **Bubble Sort**: Simple comparison-based sorting
- **Custom Sorting**: Greatest/Least value identification

```python
from Sorting_Tests import sortingTest

numbers = [64, 34, 25, 12, 22, 11, 90]
score = sortingTest.sortingTest(numbers)
print(f"Sorting Score: {score}")
```

### 3. Algorithmic Tests
Complex computational challenges:
- **Prime Counter**: Count prime numbers up to N
- **Wave Function**: Quantum mechanics calculations

```python
from Algorthmic_Tests import primeCounter

primes = primeCounter.primeCounter(1001)
```

### 4. AI/ML Benchmarks
Test neural network performance with multiple models:

#### Available Models:
- **SimpleNeuralNet**: Basic feedforward network
- **RNN**: Recurrent Neural Network
- **LargeNeuralNet**: Complex LSTM-based architecture
- **HuggingFace Models**: Load and test any HuggingFace model

#### Supported Devices:
- CPU (default)
- CUDA (NVIDIA GPUs)
- XPU (Intel GPUs) - **Warning: Was not officially tested; based off Intel documentation**
- MPS
- Vulkan

```python
from AI.aiScoring import score
import torch

# Create random input tensor
data = torch.randn(32, 16)

# Test SimpleNeuralNet
result = score(data, device="cpu", test=1, inputSize=16, hx=32, outputSize=1)
print(result)

# Test HuggingFace model
result = score("Hello, world!", device="cpu", test=4, model="google/gemma-3-270m", type="text-generation")
print(result)
```

#### Training Your Own Model:
```python
from ScoringSysAI import traningRNNModelRunner
import torch

# Prepare your dataset
trainData = torch.randn(1000, 16)
trainLabels = torch.randn(1000, 1)

result = traningRNNModelRunner(dataset=(trainData, trainLabels), epochs=50, device="cpu", inputSize=16, hx=32)
print(result)
```

### 5. Multiprocessing Tests
Stress test with parallel processing:
- **Multi-Core Prime Counting**: Distribute prime counting across cores
- **Multi-Core Merge Sorting**: Parallel sorting operations

```python
from Multiprocessing_Tests import multiPrimeCounters

multiPrimeCounters.multiPrimeCounting(numOfCores=6, countTo=10001)
```

### 6. System Information
Retrieve comprehensive system specifications:

```python
from General_Computer_Info import generalSpecs

# Run all information gathering
generalSpecs.runALl()

# Or get specific information
cores = generalSpecs.cpuCoreCount()
cpu = generalSpecs.CPU()
ram = generalSpecs.RAMUsage()
temp = generalSpecs.getCPUTemp()
```

Available System Info:
- CPU core count (physical and logical)
- Processor type and architecture
- Operating system
- RAM usage
- CPU usage percentage
- Swap memory
- CPU temperature

### 7. Network Speed Test
Measure your internet connection:

```python
from WiFi_Test import wifi

speed = wifi.speedTest()
print(f"Average Speed: {speed}")
```

## Interactive Terminal Mode

The command-line interface provides an interactive way to run tests:

```bash
python ScoringSysCMD.py
```

You'll be prompted to:
1. Choose between AI tests or standard benchmarks
2. Select which AI model to test (if applicable)
3. Configure test parameters (input size, hidden layers, etc.)
4. Select compute device (CPU/GPU)

## Scoring System

PyPC calculates performance scores based on:
- **Execution Time**: Faster execution = higher score
- **Task Complexity**: More complex tasks weighted higher
- **Resource Efficiency**: Lower resource usage improves score

Final score formula:
```
Total Score = (Algorithm + Simple + Sorting + WiFi) / TotalTime * 0.1
```

## Advanced Usage

### Custom AI Model Testing
```python
from AI.aiTests import HuggingFace

# Load any HuggingFace model
model = HuggingFace(modelName="facebook/opt-125m", device="cuda", type="text-generation")
output = model.model("Your prompt here")
```

### Custom Neural Network Training
```python
from AI.aiTests import TrainRNNModel
import torch

# Prepare your data
xTrain = torch.randn(5000, 16)
yTrain = torch.randn(5000, 1)

# Train the model
trainer = TrainRNNModel(xTrain, yTrain, device="cpu", epochs=100, lr=0.0001, batchSize=64)
trainedModel = trainer.run(inputSize=16, hx=32)
```

## Project Structure

```
PyPC/
├── AI/                          # AI/ML benchmarking
│   ├── aiScoring.py            # Scoring system for AI tests
│   └── aiTests.py              # Neural network implementations
├── Algorthmic_Tests/           # Complex algorithms
│   ├── gobalAlgTest.py         # Global algorithm testing
│   ├── primeCounter.py         # Prime number counting
│   └── waveFunction.py         # Wave function calculations
├── General_Computer_Info/      # System information
│   └── generalSpecs.py         # Hardware specifications
├── Multiprocessing_Tests/      # Parallel processing tests
│   ├── multiMergeSorting.py    # Parallel merge sort
│   └── multiPrimeCounters.py   # Parallel prime counting
├── Simple_Tests/               # Basic performance tests
│   ├── simpleTests.py          # Test orchestration
│   └── *.py                    # Individual test files
├── Sorting_Tests/              # Sorting algorithms
│   ├── sortingTest.py          # Test orchestration
│   └── *.py                    # Individual sorting algorithms
├── WiFi_Test/                  # Network speed testing
│   └── wifi.py                 # Speed test implementation
├── ScoringSys.py               # Main scoring system (non-AI)
├── ScoringSysAI.py             # AI training scoring
└── ScoringSysCMD.py            # Command-line interface
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under CC0 1.0 Universal - see the [LICENSE](LICENSE) file for details.

---

Made by Mitchell Shibilski-Unkel
