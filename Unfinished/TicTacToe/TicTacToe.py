import random
import numpy as np
import json

class TicTacToePlayer:
    def __init__(self, name):
    
    def makePlayer(hiddenLayers,name):
        newPlayer = TicTacToePlayer(name)
        
        hiddenLayers.append(9)
        
        newPlayer.networkWeights.append(np.zeros((9,hiddenLayers[0])))
        print(newPlayer.networkWeights)
        return newPlayer
            
        
        # for numNodes in range(1,len(hiddenLayers)):
            
        
        # inputArr = []
        # for i in range(9):
        #     inputArr.append(0) 
        # newPlayer.network.append(np.array(inputArr))
        
        # outputArr = []
        # for i in range(9):
        #     outputArr.append(0) 
        # newPlayer.inputLayers = np.array(outputArr)
        
        # hiddenArr = []
        # for l in hiddenLayers:
        #     newArr = []
        #     for i in range(l):
        #         newArr.append(0)
        #     hiddenArr.append
        
    
    
    # def exportToJson()
            
            
            

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
        self.board[spotIndex] = playerNumber
        
    def whoWon(self):
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
            return self.board[3]
        if (self.board[6] == self.board[7] and self.board[7] == self.board[8] and self.board[6] != 0):
            return self.board[6]
        
        #check diagonal
        if (self.board[0] == self.board[4] and self.board[4] == self.board[8] and self.board[0] != 0):
            return self.board[0]
        if (self.board[2] == self.board[4] and self.board[4]== self.board[6] and self.board[6] != 0):
            return self.board[2][0]
        
        return 0
        
    def placeRandom(self, playerNumber):
        randomI = random.randrange(0,9)
        while self.board[randomI] != 0:
            randomI = random.randrange(0,9)
            
        self.board[randomI] = playerNumber
        
                
        
def main():
    game = TicTacToeGame()
    game.printSymbolBoard()
        
if __name__ == "__main__":
    main()