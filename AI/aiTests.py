from torch import nn


class SimpleNeuralNet(nn.Module):
    def __init__(self, inputSize: int = 16, hx: int = 32, outputSize: int = 1):
        super(SimpleNeuralNet, self).__init__()
        self.inputSize = inputSize
        self.hx = hx
        self.outputSize = outputSize
        
    def forward(self, x):
        net = nn.Sequential(
            nn.Linear(self.inputSize, self.hx),
            nn.ReLU(),
            nn.Linear(self.hx, self.outputSize),
            nn.Sigmoid()
        )
        
        return net
    
class RNN(nn.Module):
    def __init__(self, inputSize: int = 16, hx: int = 32, outputSize: int = 1, numLayers: int = 24):
        super(RNN, self).__init__()
        self.inputSize = inputSize
        self.hx = hx
        self.outputSize = outputSize
        self.numLayers = numLayers
        
    def forward(self, x):
        rnn = nn.Sequential(
            nn.RNN(self.inputSize, self.hx, self.numLayers),
            nn.Linear(self.inputSize, self.hx),
            nn.ReLU(),
            nn.Linear(self.hx, self.outputSize),
            nn.Sigmoid()
        )
        
        return rnn
    
class LargeNeuralNet(nn.Module):
    def __init__(self, inputSize: int = 16, hx: int = 32, outputSize: int = 1):
        super(LargeNeuralNet, self).__init__()
        self.inputSize = inputSize
        self.hx = hx
        self.outputSize = outputSize
        
    def forward(self, x):
        net = nn.Sequential(
            nn.LSTM(self.inputSize, self.hx, self.outputSize, bidirectional=True),
            nn.Linear(self.inputSize, self.hx),
            nn.ReLU(),
            nn.Linear(self.hx, self.outputSize),
            nn.ReLU(),
            nn.Linear(self.hx, self.outputSize),
            nn.ReLU(),
            nn.Linear(self.hx, self.outputSize),
            nn.ReLU(),
            nn.Linear(self.hx, self.outputSize),
            nn.Sigmoid()
        )
        
        return net
    
class HuggingFace:
    def __init__(self, modelName: str = "google/gemma-3-270m", device: str = "cpu", type: str = "text-generation"):
        self.modelName = modelName
        self.device = device
        self.type = type
        
    def model(self, data):
        from transformers import pipeline
        pipe = pipeline(self.type, self.modelName, device=self.device)(data)
        return pipe