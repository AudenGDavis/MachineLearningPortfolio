import random
import numpy as np

class Game:

    playerX = 0
    playerY = 0

    field = None

    def __init__(self):
        self.generateField()

    def printField(self):
        print("╔", end="")
        for i in range(len(self.field[0])):
            print("═", end="")
        print("╗")

        for y in range(len(self.field)):
            print("║", end="")
            for x in range(len(self.field[y])):
                if x == self.playerX and y == self.playerY:
                    print("♟", end="")
                elif self.field[y][x] == 0:
                    print(" ", end="")
                else:
                    print("✘", end="")
            print("║")

        print("╚", end="")
        for i in range(len(self.field[0])):
            print("═", end="")
        print("╝")

    def moveUp(self):
        if self.field == None:
            return 0
        if self.playerY == 0:
            return 0
        if self.field[self.playerY-1][self.playerX] == 1:
            return 0
        
        self.playerY -= 1
        return 1
    
    def moveDown(self):
        if self.field == None:
            return 0
        if self.playerX == len(self.field):
            return 0
        if self.field[self.playerY+1][self.playerX] == 1:
            return 0
        
        self.playerY += 1
        return 1
    
    def moveRight(self):
        if self.field == None:
            return 0
        if self.playerY == len(self.field[0]):
            return 0
        if self.field[self.playerY][self.playerX+1] == 1:
            return 0
        
        self.playerX += 1
        return 1
    
    def moveLeft(self):
        if self.field == None:
            return 0
        if self.playerX == 0:
            return 0
        if self.field[self.playerY][self.playerX-1] == 1:
            return 0
        
        self.playerX -= 1
        return 1

    def generateField(self):
        returnField = [[0 for _ in range(10)] for _ in range(10)] #makes a blank 10x10 2d array

        for i in range(10):
            returnField[random.randint(0,9)][random.randint(1,8)] = 1 #places a mine randomly, but not in colums 0 and 9 (safe zones)

        self.field = returnField


def main():
    mat1 = np.array([[1,2]])
    
    mat2 = np.array([[1,2],
                     [0,0]])
    
    mat3 = np.array([[1,1]])
    print(np.matmul(mat1,mat2) + mat3)

if __name__ == "__main__":
    main()

