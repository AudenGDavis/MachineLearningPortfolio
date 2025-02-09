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
    def runMatchUp(player1: TicTacToePlayer, player2: TicTacToePlayer, iterations: int, player1Name: str,player2Name: str): # returns playerId of who won the matchup
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
                
        
        print("Player 1 ("+ str(player1Name)+ "): \n\tTotal Points: " + str(player1Points) + "\n\tAverage: "+ str(float(player1Points)/iterations))
        print("Player 2 ("+ str(player2Name)+ "): \n\tTotal Points: " + str(player2Points) + "\n\tAverage: "+ str(float(player2Points)/iterations))
        
        return player1Points, player2Points
     
     
     
def main():
    # 1/15 1 Model =>    exports/01-15-2025_09-12-48AM/Generation1000/Network1
    # 1/15 2 Model =>    exports/01-15-2025_11-02-10AM/Generation1000/Network0
    # blank Model =>    exports/blank.json
    # 1/8 Model =>    exports/01-08-2025_07-16-14PM/Generation700000/Network14
    # print()
    # player1Path = sys.argv[1]
    # player2Path = sys.argv[2]
    # botPlayer1: TicTacToePlayer = TicTacToePlayer(AudensNeuralNetworkLibrary.NeuralNetwork.importFromJson(player1Path))
    # botPlayer2: TicTacToePlayer = TicTacToePlayer(AudensNeuralNetworkLibrary.NeuralNetwork.importFromJson(player2Path))
    # MatchUp.runMatchUp(botPlayer1,botPlayer2,100000,player1Path,player2Path)
    # print()
    
    # gets best network
    highest = 0
    index = 0
    sum = 0
    for i in range(100):
        print("------------------------------------------------------")
        player1Path = "exports/01-18-2025_04-39-56PM/Generation10000/Network" + str(i)
        player2Path = "exports/goodModel.json"
        botPlayer1: TicTacToePlayer = TicTacToePlayer(AudensNeuralNetworkLibrary.NeuralNetwork.importFromJson(player1Path))
        botPlayer2: TicTacToePlayer = TicTacToePlayer(AudensNeuralNetworkLibrary.NeuralNetwork.importFromJson(player2Path))
        player1Points, player2Points = MatchUp.runMatchUp(botPlayer1,botPlayer2,1000,player1Path,player2Path)
        sum += player1Points
        if player1Points > highest:
            highest = player1Points
            index = i
            
    print(sum/100)
    print("best model: exports/01-15-2025_05-04-05PM/Generation10000/Network"+str(index))
        
    
        
if __name__ == "__main__":
    main()