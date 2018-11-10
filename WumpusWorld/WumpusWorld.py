from texttable import Texttable

class GameWorld:
    
    def __init__(self, name = "Player"):
        self.name = name
        self.world = list()

    def displayEntireWorld(self):
        '''This should display the game state to the screen'''
        print("This is entire World")
        table = Texttable(30)
        table.set_cols_align([
			"c", "c", "c", "c", "c"
			]
		)
        table.set_cols_width([
			3, 3, 3, 3, 3
			]
		)
        table.add_rows([[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5]],header=False)
        print(table.draw())
    
    def displayVisibleWorld(self):
        '''Displays all squares one away from the player'''
        print("Visible World")
        pass

    def moveForward(self):
        '''Move the player forward one square in the direction they are facing'''
        print("Forward")
        pass
    
    def turnLeft(self):
        '''Turn the player 90 degrees to the left'''
        print("Left")
    
    def turnRight(self):
        '''Turn the player 90 degrees to the right'''
        print("Right")
        pass
    
    def haveIWon(self):
        '''returns true or false if the player has won'''
        print("Won")
        pass
    
    def amIAlive(self):
        '''returns true or false depending on if player hit a wumpus or pit'''
        print("Alive")
        pass

    def quit(self):
        print("Quit")

    def showHelp(self):
        print("\tWelcome To the WUMPUS WORLD\n\n \
        How to play the game:\n \
        a or A should turn the player to the left\n \
        d or D should turn the player to the right\n \
        w or W should move the player forward\n \
        c or C should cheat and show the entire state\n \
        \tof the game using displayEntireWorld\n \
        q or Q should end the game\n \
        ")
        print("__________________________________________________________")
    
    def gameStart(self):
        print("Hi " + self.name+"!")
        print("__________________________________________________________")