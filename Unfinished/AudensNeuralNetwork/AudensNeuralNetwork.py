import numpy as np


class NeuralNetwork:
    def __init__(self, nodes: list[float]):
        self.structure = nodes.copy()
        self.networkWeights = []
        for layerIndex in range(1,len(nodes)):
            self.networkWeights.append(np.ones((nodes[layerIndex-1],nodes[layerIndex])))
            
        self.networkBiases = []
        for layerIndex in range(1,len(nodes)):
            self.networkBiases.append(np.ones((nodes[layerIndex])))

    def computeNetwork(self, inputArr: list[float]):
        layerActivations = inputArr
        for i in range(len(self.networkWeights)):
            layerActivations = np.matmul(layerActivations,self.networkWeights[i]) + self.networkBiases[i]
            
        return layerActivations
    
    def exportNetworkAsDictionary(self):
        returnDict = {"structure": self.structure}
        lay
        
network = NeuralNetwork([3,2])
print(network.computeNetwork([1.0,2.0,1.0]))