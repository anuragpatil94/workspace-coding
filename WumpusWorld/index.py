from WumpusWorld import GameWorld
import os

import msvcrt

def start():
    name = input("Enter Your Name: ")
    gameWorld = GameWorld(name)
    gameWorld.gameStart()   
    gameWorld.showHelp()

    _start = str(input("Do you want to start the game?(y/n) "))
    if(_start.lower() == "y" or _start.lower() == "yes"):
        
        gameWorld.createWorld()
        os.system('cls')
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
        close = input("press close to exit")

def game(gameWorld, inputValue):
    switcher = {
        "a" : gameWorld.moveLeft,
        "d" : gameWorld.moveRight,
        "w" : gameWorld.moveForward,
        "s" : gameWorld.moveBack,
        "c" : gameWorld.displayEntireWorld,
        "v" : gameWorld.displayVisibleWorld,
    }
    
    return switcher.get(inputValue.lower(), lambda: "Invalid Input")()
    
    
start()