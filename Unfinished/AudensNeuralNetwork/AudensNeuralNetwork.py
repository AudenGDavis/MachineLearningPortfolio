import numpy as np
import json
import time
from datetime import datetime
import os
import random

#chatGPT generated function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# ChatGPT generated function
def getFormattedTime():
    # Get the current time in the machine's timezone
    current_time = datetime.now()
    # Format the time as [mm/dd/yyyy/]-[time in timezone that the machine is running in]
    formatted_time = current_time.strftime("%m-%d-%Y_%I-%M-%S%p%Z")
    return formatted_time

class NeuralNetwork:
    def __init__(self, nodes: list[float]):
        self.structure = nodes.copy()
        self.networkWeights: list[np.ndarray] = []
        for layerIndex in range(1,len(nodes)):
            self.networkWeights.append(np.ones((nodes[layerIndex-1],nodes[layerIndex])))
            
        self.networkBiases: list[np.ndarray] = []
        for layerIndex in range(1,len(nodes)):
            self.networkBiases.append(np.ones((nodes[layerIndex])))

    def computeNetwork(self, inputArr: list[float]):
        layerActivations = inputArr
        for i in range(len(self.networkWeights)):
            layerActivations = np.matmul(layerActivations,self.networkWeights[i]) + self.networkBiases[i]
            
        return layerActivations
    
    def exportNetworkAsDictionary(self):
        returnDict = {"structure": self.structure}
        
        returnWeightMatrices = []
        for i in self.networkWeights:
            returnWeightMatrices.append(i.tolist())
            
        returnDict["networkWeights"] = returnWeightMatrices
            
        returnBiasMatrices = []
        for i in self.networkBiases:
            returnBiasMatrices.append(i.tolist())
        
        returnDict["networkBiases"] = returnBiasMatrices
        
        return returnDict
    
    def exportNetworkAsJson(self, fileName: str):
        os.makedirs(os.path.dirname(fileName), exist_ok=True)
        with open(fileName, "w") as file:
            file.write(json.dumps(self.exportNetworkAsDictionary()))
            
    def importFromJson(fileName:str) -> "NeuralNetwork":
        with open(fileName, 'r') as file:
            data = json.load(file)

        network = NeuralNetwork(data["structure"])
        for i in data["networkBiases"]:
            network.networkBiases.append(np.array(i))
            
        for i in data["networkWeights"]:
            network.networkBiases.append(np.array(i))
        return network
    
    def getOffSpring(self,numMutations: int, mutationAmount: float) -> "NeuralNetwork":
        network = NeuralNetwork(self.structure)
        
        dict = network.exportNetworkAsDictionary()
        
        network = NeuralNetwork(dict["structure"])
        network.networkBiases = []
        network.networkWeights = []
        for i in dict["networkBiases"]:
            network.networkBiases.append(np.array(i))
            
        for i in dict["networkWeights"]:
            network.networkWeights.append(np.array(i))
            
        # for i in range(numMutations):
        #     #mutate bias or weight:
        #     if 1 == 1: # 1 = mutate weight random.randrange(0,2)
        #         layerWeights: int = random.randrange(0,len(self.networkWeights))
                
        #         height, width = self.networkWeights[layerWeights].shape
                
        #         network.networkWeights[layerWeights][random.randrange(height),random.randrange(width)]+= mutationAmount
        return network
    
# network: NeuralNetwork = NeuralNetwork([3,2,3])
# network.exportNetworkAsJson("exports/"+getFormattedTime()+".json")

network: NeuralNetwork = NeuralNetwork.importFromJson("exports/12-04-2024_11-09-52AM.json")
print(network.exportNetworkAsDictionary())  
print(network.getOffSpring(1,1).exportNetworkAsDictionary())    
                

        
