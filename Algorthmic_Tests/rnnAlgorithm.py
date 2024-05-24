from torch import nn
from torch import Tensor


def RNN(values: list, inputSize: int, hiddenSize: int, numLayers: int, useGPU: bool = False):
    if useGPU == True:
        rnn = nn.RNN(inputSize, hiddenSize, numLayers).to("cuda")
    else:
        rnn = nn.RNN(inputSize, hiddenSize, numLayers).to("cpu")
        
    final = rnn(Tensor(values))
        
    return final