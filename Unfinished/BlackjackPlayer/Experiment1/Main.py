import random

class Card:
    
    def __init__(self, face: str, suit: str):
        self.suit = suit
        self.face = face
        self.count = self.getCount(face)

    def getString(self):
        return self.face + " of " + self.suit
    
    def getStringShort(self):
        return self.face[0] + self.getSuitSymbol()
    
    def getCountValue(self):
        return self.count
    
    def getCount(self,face: str) -> list[int] :
        cardTable = {
            "ace": [1,11],
            "2" : [2],
            "3" : [3],
            "4" : [4],
            "5" : [5],
            "6" : [6],
            "7" : [7],
            "8" : [8],
            "9" : [9],
            "10" : [10],
            "jack" : [10],
            "queen" : [10],
            "king" : [10],
        }

        return cardTable.get(face.lower())
    
    def getSuitSymbol(self):
        if self.suit == "spades":
            return "♠"
        if self.suit == "clubs":
            return "♣"
        if self.suit == "hearts":
            return "♥"
        if self.suit == "diamonds":
            return "♦"
        else:
            return "╳"

class Game:

    deck = []

    def __init__(self, numDecks: int):
        for i in range(numDecks):
            for suit in ["spades", "clubs", "diamonds", "hearts"]:
                for face in ["ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king"]:
                    self.deck.append(Card(face, suit))

    def getDeck(self):
        return self.deck

    def getString(self) -> str:
        string = "Deck:"
        for card in self.deck:
            string += " " + card.getStringShort() + " "

        return string
    
    def shuffle(self):
        newDeck = []
        while len(self.deck) > 0:
            index = random.randint(0,len(self.deck)-1)
            card = self.deck[index]
            self.deck.pop(index)
            newDeck.append(card)

        self.deck = newDeck
        
    def viewTopCard(self) -> str:
        if len(self.deck) > 0:
            return self.deck[0]
        
    def dealTopCard(self) -> str:
        if len(self.deck) > 0:
            card = self.deck[0]
            self.deck.pop(0)
            return card 
    
class Simulation:
    def __init__(self, hitOnSoft: bool, hitUntil: int, numDecks: int):
        self.hitOnSoft = hitOnSoft
        self.hitUntil = hitUntil
        self.game = Game(numDecks)
        
    def playGame(self) -> bool: #true means the player won, false means the player lost
        playerHand = [self.game.dealTopCard()]
        dealerHand = [self.game.dealTopCard()]
        Simulation.getHandCount(playerHand())
        
    def getHandCount(hand: list[Card]) -> int:
        options = [0]
        for card in hand:
            if len(card.count) == 2:
                newOptions = [0]
                for baseCount in options:
                    for newCount in card.getCountValue():
                        newOptions.append(baseCount + newCount)
                options = newOptions
                
        

def Main():
    options = [0]
    for card in [Card("ace","clubs"),Card("ace","diamonds")]:
        newOptions = []
        for baseCount in options:
            for newCount in card.getCountValue():
                newOptions.append(baseCount + newCount)
        options = newOptions
        
    print(options)
    
    # myGame = Game(1)
    # myGame.shuffle()
    # print(myGame.getString())




    

if __name__ == "__main__":
    Main()