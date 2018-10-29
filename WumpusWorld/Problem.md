# WUMPUS WORLD

In this assignment you will be using a class to play a game where you explore a small world. The trick is that all interactions with this world should be done through public methods to manipulate the internal data.

## Specification

The game is played on a 5x5 grid.

The grid contains a

- **player** (you),
- a **wumpus** (the enemy!),
- a **pot of gold** (reward)
- some **pits** (random number from 5 - 10).

Moving over a pit or onto a wumpus loses the game. Moving over the gold wins you the game.

The state of the game should be stored in a class called GameWorld. A private field of that class should be a 2-dimensional array of size 5. This array should store the state of the game. As this is a class, you should have at least the following public members:

GameWorld(...) // constructor that creates the game with a random startup

displayEntireWorld(...) // This should display the game state to the screen

displayVisibleWorld(...) // Displays all squares one away from the player

moveForward(...) // Move the player forward one square in the direction they are facing

turnLeft(...) // Turn the player 90 degrees to the left

turnRight(...) // Turn the player 90 degrees to the
right

haveIWon() // returns true or false if the player has won

amIAlive() // returns true or false depending on if player hit a wumpus or pit

### Task

Your code should allow the player to, starting from a random location, explore the game world. So start by creating an object of GameWorld in main (which should call the constructor which sets up a random instance of the world. Then display the visible world and display a menu letting the user make some moves.

This menu should take the following input:

- a or A should turn the player to the left
- d or D should turn the player to the right
- w or W should move the player forward
- c or C should cheat and show the entire state of the game using displayEntireWorld
- q or Q should end the game

After implementing the appropriate action, your code should check to see if it is over a wumpus or a pit, or if it has won by getting the gold. Display the results. You should then loop over this code until either the player finds the gold or dies. You should also display appropriate error messages if the player tries to move in an invalid direction (tries to leave the board).

Take care to use appropriate access specifiers. Do not simply make everything public and work in main. You should try as much as possible to only use the methods that I have specified as public. Your methods internal to the class should then manipulate the appropriate data.
