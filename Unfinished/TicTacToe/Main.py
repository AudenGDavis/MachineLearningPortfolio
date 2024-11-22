import random
import numpy as np
import json

class TicTacToePlayer:
    def __init__(self, name):
        self.inputLayers = None
        self.hiddenLayers = None
        self.outputLayers = None
    
    def importFromJson()
            
            
            

class TicTacToeGame:
    
    def __init__(self):
        self.board = []
        for i in range(3):
            self.board.append([0,0,0]) # 0 = neutral, 1 = player 1 mark, -1 = opponent -1 mark 
    
    def getSymbol(num): # 1 = X , -1 = O:
        if num == 1:
            return "X"
        elif num == -1:
            return "O"
        
        return " "

    def printNumBoard(self):
        print(" " + str(self.board[0][0]) + " ┃ " + str(self.board[0][1]) + " ┃ " + str(self.board[0][2]) + " ")
        print("━━━╋━━━╋━━━")
        print(" " + str(self.board[1][0]) + " ┃ " + str(self.board[1][1]) + " ┃ " + str(self.board[1][2]) + " ")
        print("━━━╋━━━╋━━━")
        print(" " + str(self.board[2][0]) + " ┃ " + str(self.board[2][1]) + " ┃ " + str(self.board[2][2]) + " ")
       
    def printSymbolBoard(self): # 1 = X , -1 = O
        print(" " + str(TicTacToeGame.getSymbol(self.board[0][0])) + " ┃ " + str(TicTacToeGame.getSymbol(self.board[0][1])) + " ┃ " + str(TicTacToeGame.getSymbol(self.board[0][2])) + " ")
        print("━━━╋━━━╋━━━")
        print(" " + str(TicTacToeGame.getSymbol(self.board[1][0])) + " ┃ " + str(TicTacToeGame.getSymbol(self.board[1][1])) + " ┃ " + str(TicTacToeGame.getSymbol(self.board[1][2])) + " ")
        print("━━━╋━━━╋━━━")
        print(" " + str(TicTacToeGame.getSymbol(self.board[2][0])) + " ┃ " + str(TicTacToeGame.getSymbol(self.board[2][1])) + " ┃ " + str(TicTacToeGame.getSymbol(self.board[2][2])) + " ")

    def placeMark(self, playerNumber: int, rowIndex: int, columnIndex: int):
        self.board[rowIndex][columnIndex] = playerNumber
        
    def whoWon(self):
        #check horizontal
        if (self.board[0][0] == self.board[0][1] and self.board[0][1] == self.board[0][2] and self.board[0][0] != 0):
            return self.board[0][0]
        if (self.board[1][0] == self.board[1][1] and self.board[1][1] == self.board[1][2] and self.board[1][0] != 0):
            return self.board[1][0]
        if (self.board[2][0] == self.board[2][1] and self.board[2][1] == self.board[2][2] and self.board[2][0] != 0):
            return self.board[2][0]
        
        #check vertical
        if (self.board[0][0] == self.board[1][0] and self.board[1][0] == self.board[2][0] and self.board[0][0] != 0): 
            return self.board[0][0]
        if (self.board[0][1] == self.board[1][1] and self.board[1][1] == self.board[2][1] and self.board[0][1] != 0):
            return self.board[0][1]
        if (self.board[0][2] == self.board[1][2] and self.board[1][2] == self.board[2][2] and self.board[0][2] != 0):
            return self.board[2][2]
        
        #check diagonal
        
        if (self.board[0][0] == self.board[1][1] and self.board[1][1] == self.board[2][2] and self.board[2][2] != 0): 
            return self.board[0][0]
        if (self.board[2][0] == self.board[1][1] and self.board[1][1] == self.board[0][2] and self.board[0][2] != 0):
            return self.board[2][0]
        
        return 0
        
    def placeRandom(self, playerNumber):
        randomR = random.randrange(0,3)
        randomC = random.randrange(0,3)
        while self.board[randomR][randomC] != 0:
            randomR = random.randrange(0,3)
            randomC = random.randrange(0,3)
            
        self.board[randomR][randomC] = playerNumber
        
                
        
def main():
    player = TicTacToePlayer([1],"1")
        
if __name__ == "__main__":
    main()