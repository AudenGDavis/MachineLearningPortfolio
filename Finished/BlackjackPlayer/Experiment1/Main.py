import random
class Hand:
    def __init__(self, cards):
        self.cards = cards
    
    def getCards(self):
        return self.cards
    
    def printHand(self):
        for card in self.cards:
            print(" - " + card.getString())
       
    def addCard(self, card):
        self.cards.append(card)

    def getCount(self):
        options = [0]
        for card in self.cards:
            newOptions = []
            for baseCount in options:
                for newCount in card.getCountValue():
                    newOptions.append(baseCount + newCount)
            options = newOptions
        return newOptions
    
    def getHighest(self) -> int:
        highest = -1
        for i in self.getCount():
            if i <= 21 and i > highest:
                highest = i
                continue
        return(highest)
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
        self.Deck = []
        for i in range(numDecks):
            for suit in ["spades", "clubs", "diamonds", "hearts"]:
                for face in ["ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king"]:
                    self.deck.append(Card(face, suit))

    def getDeck(self):
        return self.deck

    def getString(self) -> str:
        string = "Deck: \n"
        for card in self.deck:
            string += " " + card.getString() + ", "

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
        self.numDecks = numDecks
        self.deck = []
        for i in range(numDecks):
            for suit in ["spades", "clubs", "diamonds", "hearts"]:
                for face in ["ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king"]:
                    self.deck.append(Card(face, suit))
                    
    def getDeck(self):
        return self.deck

    def getStringDeck(self) -> str:
        string = "Deck: \n"
        for card in self.deck:
            string += " " + card.getString() + ", "

        return string
    
    def shuffle(self):
        newDeck = []
        while len(self.deck) > 0:
            index = random.randint(0,len(self.deck)-1)
            card = self.deck[index]
            self.deck.pop(index)
            newDeck.append(card)

        self.deck = newDeck
        
    def viewTopCard(self) -> Card:
        if len(self.deck) > 0:
            return self.deck[0]
        
    def dealTopCard(self) -> Card:
        if len(self.deck) > 0:
            card = self.deck[0]
            self.deck.pop(0)
            return card                  
        
    def playGame(self) -> int: #2 means the player won, 0 means the player lost, 1 means the player pushed
        self.shuffle()
        playerHand = Hand([self.dealTopCard(),self.dealTopCard()])
        dealerHand = Hand([self.dealTopCard()])
        
        if playerHand.getCount()[-1] == 21:
            return True
        if not self.hitOnSoft:
            while playerHand.getCount()[-1] < self.hitUntil:
                playerHand.addCard(self.dealTopCard())
        else:
            while playerHand.getCount()[0] < self.hitUntil:
                playerHand.addCard(self.dealTopCard())
            
        if playerHand.getHighest() == -1:
            return 0
    
        # dealer hits on soft 17
        while dealerHand.getCount()[0] < 17:
            dealerHand.addCard(self.dealTopCard())
        if dealerHand.getHighest() > playerHand.getHighest():
            return(0)
        elif dealerHand.getHighest() < playerHand.getHighest():
            return(2)
        elif dealerHand.getHighest() == playerHand.getHighest():
            return(1)
        
def Main():
    highestS = None
    highestT = None
    highestWinRate = 0
    
    numDecks = 1
    iterations = 50000
    for s in [True,False]:
        for t in [10,11,12,13,14,15,16,17,18,19,20]:
            winSum = 0.0
            tieSum = 0.0
            loseSum = 0.0
            for i in range(iterations):
                sim = Simulation(s,t,numDecks)
                result = sim.playGame()
                if result == 2: 
                    winSum += 1.0
                if result == 1: 
                    tieSum += 1.0
                if result == 0: 
                    loseSum += 1.0
            if winSum/float(iterations) > highestWinRate:
                highestT = t
                highestS = s
                highestWinRate = winSum/float(iterations)
            print("HitUntil: " + str(t) + ", Hit on Soft: " + str(s) )
            print(" - Percent Wins: " + str(winSum/float(iterations)))
            print(" - Percent Ties: " + str(tieSum/float(iterations)))
            print(" - Percent Losses: " + str(loseSum/float(iterations)))
            
    
    print("------------------------------------")
    print("Best Strategy: ")
    print(" - Hit Until: " + str(highestT))
    print(" - Hit On Soft: " + str(highestS))
    print(" - Win Rate: " + str(highestWinRate))
    print("Iterations: " + str(iterations))
    print("------------------------------------")
                    
                
                
    

if __name__ == "__main__":
    Main()