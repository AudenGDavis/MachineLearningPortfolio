import TicTacToe

def whosTurn(player):
    if player == 1:
        return 1
    else:
        return 2


game = TicTacToe.TicTacToeGame()

turn = 1

isDone = False
while not isDone:
    game.printSymbolBoard()
    print()
    move = input("Player " + str(whosTurn(turn)) + ", what is your move? ")
    game.placeMark(turn,int(move))
    
    winner = game.whoWon()
    if winner != 0:
        print(("Player " + str(whosTurn(turn)) + " won"))
        isDone = True
    else:
        print()
    turn *= -1