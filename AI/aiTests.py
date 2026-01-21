from torch import nn
from torch.optim import Adam
from transformers import pipeline


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
    def __init__(self, inputSize: int = 16, hx: int = 32, outputSize: int = 1, bidirectional: bool = True):
        super(LargeNeuralNet, self).__init__()
        self.inputSize = inputSize
        self.hx = hx
        self.outputSize = outputSize
        self.bidirectional = bidirectional
        
    def forward(self, x):
        net = nn.Sequential(
            nn.LSTM(self.inputSize, self.hx, self.outputSize, bidirectional=self.bidirectional),
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
    
class TrainRNNModel:
    def __init__(self, datasetIn, datasetOut, device: str = "cpu", epochs: int = 50, lr: float = 0.00001, batchSize: int = 32):
        self._in = datasetIn
        self._out = datasetOut
        self.device = device
        self.epochs = epochs
        self.lr = lr
        self.batchSize = batchSize  
        
    def run(self, inputSize: int = 16, hx: int = 32):
        RNN = nn.Sequential(
            nn.RNN(inputSize, hx, 25),
            nn.Linear(self.inputSize, self.hx),
            nn.ReLU(),
            nn.Linear(self.hx, 1),
            nn.Sigmoid()
        ).to(self.device)
        
        criterion = nn.MSELoss()
        optimizer = Adam(RNN.parameters(), lr=self.lr)
        
        for epoch in range(self.epochs):
            for i in range(0, len(self._in), self.batchSize):
                inputs = self._in[i:i+self.batchSize].to(self.device)
                target = self._out[i:i+self.batchSize].to(self.device)
                
                optimizer.zero_grad()
                
                outputs = RNN(inputs)
                loss = criterion(outputs, target)
                
                loss.backward()
                optimizer.step()
            
            print(f"Epoch: {epoch+1}/{self.epochs} Loss: {loss.item()}")
            
        return RNN
    
class HuggingFace:
    def __init__(self, modelName: str = "google/gemma-3-270m", device: str = "cpu", type: str = "text-generation"):
        self.modelName = modelName
        self.device = device
        self.type = type
        
    def model(self, data):
        pipe = pipeline(self.type, self.modelName, device=self.device)(data)
        return pipe