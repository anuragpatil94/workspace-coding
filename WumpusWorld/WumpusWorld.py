from texttable import Texttable
from random import randint


class Coordinate:
    def __init__(self, coordinate=(0, 0)):
        self.x = coordinate[0]
        self.y = coordinate[1]

    def validateCoordinate(self, coordinate):
        min = 0
        max = 4
        if (coordinate[0] < 0 or coordinate[0] > 4):
            return False
        if (coordinate[1] < 0 or coordinate[1] > 4):
            return False

        return True


class GameWorld:
    _PLAYER = "A"
    _WUMPUS = "W"
    _GOLD = "G"
    _PIT = "P"

    __seen = set()

    def __init__(self, name="Player"):
        self.name = name
        self.world = [[" "]*5 for _ in range(5)]
        self.positionA = ""
        self.positionW = ""
        self.positionG = ""

    def displayEntireWorld(self):
        '''This should display the game state to the screen'''
        print("This is Entire World")
        self.__createTable(self.world)

    def displayVisibleWorld(self):
        '''Displays all squares one away from the player'''
        print("Visible World")
        visibleWorld = [[" "]*5 for _ in range(5)]
        # Player Position Coordinate
        xPos = self.positionA.x
        yPos = self.positionA.y
        visibleArray = []
        visibleDistanceArray = [-1, 0, 1]

        for x in visibleDistanceArray:
            for y in visibleDistanceArray:
                if(Coordinate.validateCoordinate(Coordinate, [xPos+y, yPos+x])):
                    visibleArray.append(Coordinate([xPos+y, yPos+x]))

        for coordinate in visibleArray:
            visibleWorld[coordinate.x][coordinate.y] = self.world[coordinate.x][coordinate.y]

        self.__createTable(visibleWorld)

    def __createTable(self,world):
        table = Texttable(30)
        table.set_cols_align(["c", "c", "c", "c", "c"])
        table.set_cols_width([3, 3, 3, 3, 3])
        table.add_rows(world, header=False)
        print(table.draw())

    def moveForward(self):
        '''Move the player forward one square in the direction they are facing'''
        print("Forward")
        self.world[self.positionA.x - 1][self.positionA.y] = self._PLAYER
        self.world[self.positionA.x][self.positionA.y] = " "
        self.positionA = Coordinate([self.positionA.x - 1, self.positionA.y])
        self.displayVisibleWorld()
        pass

    def turnLeft(self):
        '''Turn the player 90 degrees to the left'''
        print("Left")

        self.world[self.positionA.x][self.positionA.y - 1] = self._PLAYER
        self.world[self.positionA.x][self.positionA.y] = " "
        self.positionA = Coordinate([self.positionA.x, self.positionA.y - 1])
        self.displayVisibleWorld()

    def turnRight(self):
        '''Turn the player 90 degrees to the right'''
        print("Right")
        self.world[self.positionA.x][self.positionA.y + 1] = self._PLAYER
        self.world[self.positionA.x][self.positionA.y] = " "
        self.positionA = Coordinate([self.positionA.x, self.positionA.y + 1])
        self.displayVisibleWorld()

    def moveBack(self):
        '''Turn the player 90 degrees to the right'''
        print("Back")
        self.world[self.positionA.x + 1][self.positionA.y] = self._PLAYER
        self.world[self.positionA.x][self.positionA.y] = " "
        self.positionA = Coordinate([self.positionA.x + 1, self.positionA.y])
        self.displayVisibleWorld()

    def haveIWon(self):
        '''returns true or false if the player has won'''
        print("Won")
        pass

    def amIAlive(self):
        '''returns true or false depending on if player hit a wumpus or pit'''
        print("Alive")
        pass

    def createWorld(self):
        coordinateValue = self.__generateCoordinates()
        initialPosition = {
            "player": Coordinate(next(coordinateValue)),
            "wumpus": Coordinate(next(coordinateValue)),
            "gold": Coordinate(next(coordinateValue)),
            "pits": self.__pits()
        }

        # Create 2D Array
        for key, value in initialPosition.items():
            if(isinstance(value, list) and key == "pits"):
                for cObject in value:
                    self.world[cObject.x][cObject.y] = self._PIT
            else:
                if(key == "player"):
                    self.world[value.x][value.y] = self._PLAYER
                    self.positionA = value
                if(key == "wumpus"):
                    self.world[value.x][value.y] = self._WUMPUS
                    self.positionW = value
                if(key == "gold"):
                    self.world[value.x][value.y] = self._GOLD
                    self.positionG = value

    def __pits(self):
        coordinateValue = self.__generateCoordinates()
        numberOfPits = randint(1, 10)
        pits = list()
        while numberOfPits > 0:
            pits.append(Coordinate(next(coordinateValue)))
            numberOfPits = numberOfPits - 1
        return pits

    def __generateCoordinates(self, min=0, max=4):
        x, y = randint(min, max), randint(min, max)
        while True:
            self.__seen.add((x, y))
            yield (x, y)
            x, y = randint(min, max), randint(min, max)
            while (x, y) in self.__seen:
                x, y = randint(min, max), randint(min, max)

    def showHelp(self):
        print("\tWelcome To the WUMPUS WORLD\n\n \
        How to play the game:\n \
        a or A should turn the player to the left\n \
        d or D should turn the player to the right\n \
        w or W should move the player forward\n \
        s or S should move the player back\n \
        c or C should cheat and show the entire state\n \
        \tof the game using displayEntireWorld\n \
        q or Q should end the game\n \
        ")
        print("__________________________________________________________")

    def gameStart(self):
        print("Hi " + self.name+"!")
        print("__________________________________________________________")
