from WumpusWorld import GameWorld
import msvcrt

def start():
    gameWorld = GameWorld("Anurag")
    gameWorld.showHelp()

    _start = str(input("Do you want to start the game? "))

    if(_start.lower() == "y" or _start.lower() == "yes"):
        gameWorld.gameStart()
        gameWorld.displayVisibleWorld()

        while(1):
            inputValue = msvcrt.getch().decode("utf-8")
            if(inputValue == "q"):
                break

            game(gameWorld, inputValue)

def game(gameWorld, inputValue):
    switcher = {
        "a" : gameWorld.turnLeft,
        "d" : gameWorld.turnRight,
        "w" : gameWorld.moveForward,
        "c" : gameWorld.displayEntireWorld,
    }
    switcher.get(inputValue.lower(), lambda: "Invalid Input")()
    
start()