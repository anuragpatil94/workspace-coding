from WumpusWorld import GameWorld
import msvcrt

def start():
    gameWorld = GameWorld("Anurag")
    gameWorld.showHelp()

    _start = str(input("Do you want to start the game? "))

    if(_start.lower() == "y" or _start.lower() == "yes"):
        gameWorld.gameStart()
        gameWorld.createWorld()
        gameWorld.displayVisibleWorld()
        while(1):
            try:
                inputValue = msvcrt.getch().decode("utf-8")
                if(inputValue == "q"):
                    break
                result = game(gameWorld, inputValue)
                if result:
                    break
            except:
                print("WRONG INPUT")
                gameWorld.showHelp()
            

def game(gameWorld, inputValue):
    switcher = {
        "a" : gameWorld.turnLeft,
        "d" : gameWorld.turnRight,
        "w" : gameWorld.moveForward,
        "s" : gameWorld.moveBack,
        "c" : gameWorld.displayEntireWorld,
        "v" : gameWorld.displayVisibleWorld,
    }
    
    return switcher.get(inputValue.lower(), lambda: "Invalid Input")()
    
    
start()