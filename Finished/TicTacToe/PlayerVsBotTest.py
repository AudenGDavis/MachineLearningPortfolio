import random
import AudensNeuralNetworkLibrary as AudensNeuralNetworkLibrary 
import sys

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
            print("spcace occupied; placing randomly")
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
        



def main():
    print(sys.argv[1])
    botPlayer: TicTacToePlayer = TicTacToePlayer(AudensNeuralNetworkLibrary.NeuralNetwork.importFromJson(sys.argv[1]))
    game: TicTacToeGame = TicTacToeGame() 
    playerTurn = 1
    winner = None
    while winner == None:
        if playerTurn == 1:
            print()
            game.printSymbolBoard()
            game.placeMark(1,int(input("Your Move: "))) 
        elif playerTurn == -1:
            #player2's turn
            game.placeMark(-1,botPlayer.getMove(game,-1)) 
        else:
            print("...error...")
        playerTurn *= -1
        winner = game.whoWon()  
    print()
    game.printSymbolBoard()
    print(winner)
    
    
    
    
        
if __name__ == "__main__":
    main()