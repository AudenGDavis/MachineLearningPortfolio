import random
import numpy as np
import json
import AudensNeuralNetworkLibrary.AudensNeuralNetworkLibrary as AudensNeuralNetworkLibrary 
import os

class TicTacToePlayer:
    def __init__(self, network: AudensNeuralNetworkLibrary.NeuralNetwork):
        self.network:AudensNeuralNetworkLibrary.NeuralNetwork = network
        self.playerNum = 1
        self.numChildren = 0
        self.wins = 0
    
    def getChild(self,numMutations: int, mutationAmount: float):
        self.numChildren += 1
        return TicTacToePlayer(self.network.getOffSpring(numMutations,mutationAmount))

    def getMove(self,game: 'TicTacToeGame',playerNum: int) -> int:
        input = game.board.copy()
        if playerNum == -1: #flip values so that 1 represent the bot's own marks
            for i in range(len(input)):
                input[i] *= -1.0
        
        result: list[float] = self.network.computeNetwork(input)
        
        #get highest
        highestIndex = 0
        for i in range(len(result)):
            if result[highestIndex] < result[i]:
                highestIndex = i
        return highestIndex
                 

class TicTacToeGame:
    
    def __init__(self):
        self.board = []
        for i in range(9):
            self.board.append(0) # 0 = neutral, 1 = player 1 mark, -1 = player 2 mark
    
    def getSymbol(num): # 1 = X , -1 = O:
        if num == 1:
            return "X"
        elif num == -1:
            return "O"
        
        return " "

    def printNumBoard(self):
        print(" " + str(self.board[0]) + " ┃ " + str(self.board[1]) + " ┃ " + str(self.board[2]) + " ")
        print("━━━╋━━━╋━━━")
        print(" " + str(self.board[3]) + " ┃ " + str(self.board[4]) + " ┃ " + str(self.board[5]) + " ")
        print("━━━╋━━━╋━━━")
        print(" " + str(self.board[6]) + " ┃ " + str(self.board[7]) + " ┃ " + str(self.board[8]) + " ")
       
    def printSymbolBoard(self): # 1 = X , -1 = O
        print(" " + str(TicTacToeGame.getSymbol(self.board[0])) + " ┃ " + str(TicTacToeGame.getSymbol(self.board[1])) + " ┃ " + str(TicTacToeGame.getSymbol(self.board[2])) + " ")
        print("━━━╋━━━╋━━━")
        print(" " + str(TicTacToeGame.getSymbol(self.board[3])) + " ┃ " + str(TicTacToeGame.getSymbol(self.board[4])) + " ┃ " + str(TicTacToeGame.getSymbol(self.board[5])) + " ")
        print("━━━╋━━━╋━━━")
        print(" " + str(TicTacToeGame.getSymbol(self.board[6])) + " ┃ " + str(TicTacToeGame.getSymbol(self.board[7])) + " ┃ " + str(TicTacToeGame.getSymbol(self.board[8])) + " ")

    def placeMark(self, playerNumber: int, spotIndex: int):
        if self.board[spotIndex] != 0:
            randomI = random.randrange(0,9)
            while self.board[randomI] != 0:
                randomI = random.randrange(0,9)
            self.board[randomI] = playerNumber
        else:
            self.board[spotIndex] = playerNumber
        
    def whoWon(self) -> int:
        #check horizontal
        if (self.board[0] == self.board[1] and self.board[1] == self.board[2] and self.board[0] != 0):
            return self.board[0]
        if (self.board[3] == self.board[4] and self.board[4] == self.board[5] and self.board[3] != 0):
            return self.board[3]
        if (self.board[6] == self.board[7] and self.board[7] == self.board[8] and self.board[6] != 0):
            return self.board[6]
        
        #check vertical
        if (self.board[0] == self.board[3] and self.board[3] == self.board[6] and self.board[0] != 0):
            return self.board[0]
        if (self.board[1] == self.board[4] and self.board[4] == self.board[7] and self.board[1] != 0):
            return self.board[1]
        if (self.board[2] == self.board[5] and self.board[5] == self.board[8] and self.board[2] != 0):
            return self.board[2]
        
        #check diagonal
        if (self.board[0] == self.board[4] and self.board[4] == self.board[8] and self.board[0] != 0):
            return self.board[0]
        if (self.board[2] == self.board[4] and self.board[4]== self.board[6] and self.board[6] != 0):
            return self.board[2]
        
        #check tie
        for i in self.board:
            if i == 0:
                return None
        return 0
        



class MatchUp:
    #player1's id = 1
    #player2's id = -1
    def runMatchUp(player1: TicTacToePlayer, player2: TicTacToePlayer, iterations: int): # returns playerId of who won the matchup
        player1Points = 0
        player2Points = 0
        
        for i in range(iterations):
            game: TicTacToeGame = TicTacToeGame() 
            playerTurn = 1-2*(i%2)
            winner = None
            while winner == None:
                if playerTurn == 1:
                   #player1's turn
                   game.placeMark(1,player1.getMove(game,1)) 
                elif playerTurn == -1:
                   #player2's turn
                   game.placeMark(-1,player2.getMove(game,-1)) 
                else:
                    print("...error...")
                playerTurn *= -1
                winner = game.whoWon()   
                
            # game.printSymbolBoard()
            # print(winner, end="\n\n")
            if winner == 1:
                player1Points += 2
            elif winner == -1:
                player2Points += 2
            else:
                player1Points += 1
                player2Points += 1
                
        
        # print("Player 1 Wins: " + str(player1Points))
        # print("Player 2 Wins: " + str(player2Points))
        # print("\tPlayer 1 Wins: " + str(float(player1Points)))
        # print("\tPlayer 2 Wins: " + str(float(player2Points)))
        
        return player1Points, player2Points
        
          
class Experiment:
    def __init__(self,exportDirectory: str,generationSize:int,numSurvivors:int,returnJsonInterval:int,startingModel:str,):
        self.exportDirectory = exportDirectory
        self.experimentName = AudensNeuralNetworkLibrary.getFormattedTime()
        self.numSurvivors = numSurvivors
        self.returnJsonInterval = returnJsonInterval
        self.players : list[TicTacToePlayer] = []
        self.generationSize = generationSize
        for i in range(generationSize):
            self.players.append(TicTacToePlayer(AudensNeuralNetworkLibrary.NeuralNetwork.importFromJson(startingModel)))
        
    def runExperiment(self,maxIterations:int):
        currentGeneration = self.players.copy()
        for iteration in range(maxIterations):
            
            # # Matchups and Eliminations
            # print("Generation: " + str(i)+"/"+str(maxIterations))
            # survivingGeneration : list[TicTacToePlayer] = []
            # while len(currentGeneration) > 1:
            #     player1Index = random.randint(0,len(currentGeneration)-1)
            #     player1 = currentGeneration[player1Index]
            #     currentGeneration.pop(player1Index)
                
            #     player2Index = random.randint(0,len(currentGeneration)-1)
            #     player2 = currentGeneration[player2Index]
            #     currentGeneration.pop(player2Index)
                    
            #     result = MatchUp.runMatchUp(player1,player2,10)
                
            #     if result == 1:
            #         survivingGeneration.append(player1)
            #     else:
            #         survivingGeneration.append(player2)
            
            # # Replaces the Elimiated
            # currentGeneration: list[TicTacToePlayer] = []
            # for player in survivingGeneration:
            #     currentGeneration.append(player)
            #     currentGeneration.append(player.getChild(1,random.random()*2.0 - 1.0))
        
               
            print("Generation "+ str(iteration+1)+"/"+str(maxIterations))  
                
            scores = []
            for i in range(len(currentGeneration)):
                scores.append(0)
                
            #scoring
            for i in range(len(currentGeneration)-1):
                #shuffling
                currentGeneration = currentGeneration[0:1] + currentGeneration[len(currentGeneration)-1:len(currentGeneration)] + currentGeneration[1:len(currentGeneration)-1]
                scores = scores[0:1] + scores[len(scores)-1:len(scores)] + scores[1:len(scores)-1]
                
                # print(scores)
                
                #matchups
                for m in range(0,len(currentGeneration),2):
                    # print("\t"+str(currentGeneration[m]) + " is playing " + str(currentGeneration[m+1]))
                    players1Wins, players2Wins = MatchUp.runMatchUp(currentGeneration[m],currentGeneration[m+1],10)
                    scores[m] += players1Wins
                    scores[m+1] += players2Wins
                
                # print("\t"+str(scores))
            
            survivors: list[TicTacToePlayer] = []
            # getting top players
            for i in range(self.numSurvivors):
                highest = 0
                highestIndex = 0
                for p in range(len(currentGeneration)):
                    if scores[p] > highest:
                        highest = scores[p]
                        highestIndex = p
                
                survivors.append(currentGeneration[highestIndex])
                scores.pop(highestIndex)
                currentGeneration.pop(highestIndex)
                

            currentGeneration = []
            
            survivorIndex = 0
            # repopulating
            while len(currentGeneration) < self.generationSize-len(survivors):
                currentGeneration.append(survivors[survivorIndex].getChild(1,random.random()*0.1 - 0.05))
                survivorIndex+=1
                if survivorIndex == len(survivors):
                    survivorIndex = 0
            
            for p in survivors:
                currentGeneration.append(p)
            
            
            if (iteration+1) % self.returnJsonInterval == 0:
                for p in range(len(currentGeneration)):
                    currentGeneration[p].network.exportNetworkAsJson("./exports/" + self.experimentName + "/Generation"+str(iteration+1)+"/Network"+str(p))
             
            
            
                
            
    
            
            
                    
                
            
            
        
               
        
def main():
    experiment : Experiment = Experiment("./exports",100,20,100,"exports/goodModel.json")
    experiment.runExperiment(10000)
    
    # player1 = TicTacToePlayer(AudensNeuralNetworkLibrary.NeuralNetwork.importFromJson("exports/01-08-2025_07-16-14PM/Generation700000/Network10"))
    # player2 = TicTacToePlayer(AudensNeuralNetworkLibrary.NeuralNetwork.importFromJson("exports/01-08-2025_07-16-14PM/Generation0/Network4"))
    # MatchUp.runMatchUp(player1,player2,1)
    
    
    
    
        
if __name__ == "__main__":
    main()