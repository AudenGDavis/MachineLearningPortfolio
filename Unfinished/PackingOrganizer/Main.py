import array

def getBest(weights, values, maxWeight):
    print(values)
    if maxWeight <= 0:
        return [], [], 0
    
    if len(weights) == 1:
        if weights[0] > maxWeight:
            return [], [], 0
        else:
            sumScore = values[0]
            print(sumScore)
            return weights, values, sumScore 
        
    idealWeights = []
    idealValues = []
    sum = 0
    
    for i in range(len(weights)):
        
        remainingWeight = maxWeight - weights[i]
        testWeights = weights.copy()
        testWeights.pop(i)
        
        testValues = values.copy()
        testValues.pop(i)
        
        testWeights, testValues, sumScore = getBest(testWeights, testValues, remainingWeight)
        
        if sumScore > sum:
            idealValues = testValues
            idealWeights = testWeights
            sum = sumScore
            
    
    return weights+idealWeights, values+idealValues, sum
        
    
    
print(getBest([4,4,4],[1,2,3],100))
    